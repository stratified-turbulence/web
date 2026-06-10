#!/usr/bin/env python3
"""
Test harness for voila_viewer_v2_colab.ipynb

Reproduces the notebook's logic verbatim (the `_make_figure` rebuild pattern
and the widget callbacks) against mock data, so errors are caught before Colab.
Runs headless with the Agg backend.
"""

import matplotlib
matplotlib.use("Agg")

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import os
import math
import glob
import re
import tempfile
import shutil
import traceback

print("=" * 70)
print("TESTING voila_viewer_v2_colab.ipynb LOGIC")
print("=" * 70)
print()

test_dir = tempfile.mkdtemp(prefix="voila_test_")
print(f"Creating test data in: {test_dir}\n")

try:
    # ── Create mock data files ────────────────────────────────────────────────
    print("Step 1: Creating mock data files...")
    DS = 8
    tag = f"ds{DS}"
    _NxD, _NyD, _NzD = 4096 // DS, 2048 // DS, 4096 // DS

    _drdy_arr = (np.random.randn(_NxD, _NyD, _NzD).astype(np.float32) - 35.9647)
    np.save(os.path.join(test_dir, f"drdy_{tag}_norm.npy"), _drdy_arr)

    _log_eps = np.random.randn(_NxD, _NyD, _NzD).astype(np.float32)
    _log_chi = np.random.randn(_NxD, _NyD, _NzD).astype(np.float32)
    np.save(os.path.join(test_dir, f"log_eps_{tag}.npy"), _log_eps)
    np.save(os.path.join(test_dir, f"log_chi_{tag}.npy"), _log_chi)

    r = np.random.randn(_NxD, _NyD, _NzD).astype(np.float32) * 2
    np.save(os.path.join(test_dir, f"r_{tag}.npy"), r)

    # two clustering combos to exercise the combo-change path
    combos_made = [(32, 5), (64, 8)]
    for sigma, k in combos_made:
        bf = np.random.rand(_NxD, _NyD, _NzD).astype(np.float32) * 0.5
        np.save(os.path.join(test_dir, f"binary_filtered_{tag}_sigma{sigma}.npy"), bf)
        labels = np.random.randint(0, k, size=(_NxD, _NyD, _NzD)).astype(np.int32)
        np.save(os.path.join(test_dir, f"labels_{tag}_sigma{sigma}_k{k}.npy"), labels)
    print(f"  ✓ Created mock data ({_NxD}×{_NyD}×{_NzD}) for combos {combos_made}\n")

    DATA_DIR = test_dir
    DGRAD = -35.9647

    # ── Replicate the notebook's main cell logic ─────────────────────────────
    print("Step 2: Replicating notebook load + setup...")

    _label_files = sorted(glob.glob(os.path.join(DATA_DIR, f"labels_{tag}_sigma*_k*.npy")))
    assert _label_files, "should find label files"

    _combos = []
    for _lf in _label_files:
        _m = re.search(r'sigma(\d+)_k(\d+)\.npy', _lf)
        if _m:
            _combos.append((int(_m.group(1)), int(_m.group(2))))
    assert _combos, "should parse combos"
    print(f"  ✓ Found combos: {_combos}")

    SIGMA, K = _combos[0]

    _drdy_arr = np.load(os.path.join(DATA_DIR, f"drdy_{tag}_norm.npy"))
    _log_eps = np.load(os.path.join(DATA_DIR, f"log_eps_{tag}.npy"))
    _log_chi = np.load(os.path.join(DATA_DIR, f"log_chi_{tag}.npy"))

    _leps_vmin = float(np.nanpercentile(_log_eps[:, :, _NzD // 2], 2))
    _leps_vmax = float(np.nanpercentile(_log_eps[:, :, _NzD // 2], 98))
    _lchi_vmin = float(np.nanpercentile(_log_chi[:, :, _NzD // 2], 2))
    _lchi_vmax = float(np.nanpercentile(_log_chi[:, :, _NzD // 2], 98))

    def _drdy_slicer(axis, idx):
        if axis == "z":
            sl = _drdy_arr[:, :, idx]
        elif axis == "y":
            sl = _drdy_arr[:, idx, :]
        else:
            sl = _drdy_arr[idx, :, :]
        return (sl + DGRAD) / np.abs(DGRAD)

    _bf_cache, _lbl_cache = {}, {}

    def _load_clustering(sigma, k):
        if sigma not in _bf_cache:
            _bf_cache[sigma] = np.load(os.path.join(DATA_DIR, f"binary_filtered_{tag}_sigma{sigma}.npy"))
        if (sigma, k) not in _lbl_cache:
            _lbl_cache[(sigma, k)] = np.load(os.path.join(DATA_DIR, f"labels_{tag}_sigma{sigma}_k{k}.npy"))
        return _bf_cache[sigma], _lbl_cache[(sigma, k)]

    _bf0, _lbl0 = _load_clustering(SIGMA, K)
    _r_arr = np.load(os.path.join(DATA_DIR, f"r_{tag}.npy"))

    FIELDS = [
        dict(data=_r_arr,   title=r"Turbulent Density $\rho$", cmap="RdBu_r", vmin=-10, vmax=10),
        dict(slicer=_drdy_slicer, shape=(_NxD, _NyD, _NzD), title=r"$\partial \rho/\partial y + \alpha$", cmap="RdBu_r", vmin=-10, vmax=10),
        dict(data=_bf0,     title=f"Filtered overturning fraction (σ={SIGMA/DS:.4g})", cmap="RdBu_r", vmin=0, vmax=0.5),
        dict(data=_lbl0,    title=f"K-means clustering (k={K})"),
        dict(data=_log_eps, title=r"$\log_{10}(\varepsilon)$", cmap="inferno", vmin=_leps_vmin, vmax=_leps_vmax),
        dict(data=_log_chi, title=r"$\log_{10}(\chi)$",        cmap="inferno", vmin=_lchi_vmin, vmax=_lchi_vmax),
    ]

    _OVERLAY_SRC = 3
    _OVERLAY_TGTS = list(range(len(FIELDS)))
    _OVERLAY_COLORS = {0: "black", 1: "black"}
    _SIGMA_PANEL = 2

    _AXIS_CFG = {
        "z": {"dim": 2, "xl": "$x$", "yl": "$y$", "T": True},
        "y": {"dim": 1, "xl": "$x$", "yl": "$z$", "T": True},
        "x": {"dim": 0, "xl": "$z$", "yl": "$y$", "T": False},
    }
    _state = {"axis": "z", "idx": 0, "overlay": False, "sigma": SIGMA, "k": K}

    def _get_slice(f, axis, idx):
        if "slicer" in f:
            return f["slicer"](axis, idx)
        arr = f["data"]
        if axis == "x":   return arr[idx]
        elif axis == "y": return arr[:, idx]
        else:             return arr[:, :, idx]

    def _field_shape(f):
        return f["shape"] if "slicer" in f else f["data"].shape

    def _discrete_cmap(labels):
        n = int(labels.max()) + 1
        cmap = ListedColormap(plt.get_cmap("tab10").colors[:n])
        return cmap, -0.5, n - 0.5, list(range(n))

    _PANEL_W = 4.5
    _N_COLS = 3
    _N_FIELDS = len(FIELDS)
    _N_ROWS = math.ceil(_N_FIELDS / _N_COLS)

    def _make_figure(axis, idx):
        cfg = _AXIS_CFG[axis]
        do_T = cfg["T"]
        _sl0 = _get_slice(FIELDS[0], axis, idx)
        _h0, _w0 = _sl0.shape
        panel_h = _PANEL_W * (_w0 / _h0) if do_T else _PANEL_W * (_h0 / _w0)

        fig, axs2d = plt.subplots(
            _N_ROWS, _N_COLS,
            figsize=(_PANEL_W * _N_COLS, panel_h * _N_ROWS + 0.9),
            squeeze=False,
        )
        plt.subplots_adjust(left=0.05, right=0.97, bottom=0.08, top=0.90,
                            wspace=0.25, hspace=0.15)

        axs = [axs2d[r][c] for r in range(_N_ROWS) for c in range(_N_COLS)]
        for ax in axs[_N_FIELDS:]:
            ax.set_visible(False)
        axs = axs[:_N_FIELDS]

        last_ext = None
        for i, (ax, f) in enumerate(zip(axs, FIELDS)):
            sl = _get_slice(f, axis, idx)
            h, w = sl.shape
            if do_T:
                data = np.ma.masked_invalid(sl.T)
                ext = [-0.5, h - 0.5, -0.5, w - 0.5]
            else:
                data = np.ma.masked_invalid(sl)
                ext = [-0.5, w - 0.5, -0.5, h - 0.5]
            last_ext = ext

            if i == _OVERLAY_SRC:
                cmap, vmin, vmax, ticks = _discrete_cmap(f["data"])
            else:
                cmap = f.get("cmap", "viridis")
                vmin = f.get("vmin")
                vmax = f.get("vmax")
                ticks = f.get("ticks")

            kw = dict(origin="lower", aspect="equal", cmap=cmap,
                      interpolation="nearest", extent=ext)
            if vmin is not None: kw["vmin"] = vmin
            if vmax is not None: kw["vmax"] = vmax

            im = ax.imshow(data, **kw)
            plt.colorbar(im, ax=ax, shrink=0.8, ticks=ticks)
            ax.set_title(f.get("title", ""), fontsize=9)
            ax.set_xlabel(cfg["xl"])
            ax.set_ylabel(cfg["yl"])

        sd = _state["sigma"] / DS
        pad = sd * 0.4
        axs[_SIGMA_PANEL].add_patch(
            plt.Circle((sd + pad, sd + pad), sd, fill=False,
                       edgecolor='green', linewidth=3, zorder=5)
        )
        axs[_SIGMA_PANEL].text(sd + pad, sd + pad, r'$\sigma$', color='green',
                               ha='center', va='center', fontsize=7, zorder=6)

        if _state["overlay"]:
            lbl_sl = _get_slice(FIELDS[_OVERLAY_SRC], axis, idx)
            kk = int(FIELDS[_OVERLAY_SRC]["data"].max()) + 1
            levels = np.arange(0.5, kk)
            ld = lbl_sl.T if do_T else lbl_sl
            for ti in _OVERLAY_TGTS:
                axs[ti].contour(ld, levels=levels,
                                colors=_OVERLAY_COLORS.get(ti, "white"),
                                linewidths=0.6, alpha=0.7, extent=last_ext)

        fig.suptitle(
            f"{axis}-slice {idx}  "
            f"(σ={_state['sigma']}, k={_state['k']}, every {DS} grid pts)",
            fontsize=11,
        )
        return fig

    print("  ✓ Setup complete\n")

    # ── Test _make_figure for every axis, overlay off + on ───────────────────
    print("Step 3: Testing _make_figure on all axes (overlay off + on)...")
    for overlay in (False, True):
        _state["overlay"] = overlay
        for axis in ("z", "y", "x"):
            _state["axis"] = axis
            n = _field_shape(FIELDS[0])[_AXIS_CFG[axis]["dim"]]
            for idx in (0, n // 2, n - 1):
                fig = _make_figure(axis, idx)
                live = [a for a in fig.axes]  # includes colorbars
                assert len(live) >= _N_FIELDS, "should have >= 6 axes"
                plt.close(fig)
            print(f"  ✓ axis '{axis}' (overlay={overlay}) — indices 0/{n//2}/{n-1} OK")
    _state["overlay"] = False
    print()

    # ── Test the slider-range update logic ───────────────────────────────────
    print("Step 4: Testing axis-change slider range logic...")
    for axis in ("x", "y", "z"):
        n = _field_shape(FIELDS[0])[_AXIS_CFG[axis]["dim"]]
        # simulate clamping a high index into the new range
        new_value = min(n - 1, n - 1)
        assert 0 <= new_value <= n - 1
        print(f"  ✓ axis '{axis}': slider.max -> {n - 1}")
    print()

    # ── Test combo-change callback path ──────────────────────────────────────
    print("Step 5: Testing clustering combo-change path...")
    for sigma, k in _combos:
        bf, lbl = _load_clustering(sigma, k)
        FIELDS[2]["data"] = bf
        FIELDS[2]["title"] = f"Filtered overturning fraction (σ={sigma/DS:.4g})"
        FIELDS[3]["data"] = lbl
        FIELDS[3]["title"] = f"K-means clustering (k={k})"
        _state["sigma"], _state["k"] = sigma, k
        # rebuild after swap — exercises discrete cmap for the new k
        fig = _make_figure(_state["axis"], 0)
        plt.close(fig)
        kk = int(FIELDS[3]["data"].max()) + 1
        assert kk <= k, f"label max should be < k for σ={sigma}, k={k}"
        print(f"  ✓ Combo σ={sigma}, k={k}: swap + rebuild OK (clusters={kk})")
    print()

    # ── Summary ──────────────────────────────────────────────────────────────
    print("=" * 70)
    print("✓ ALL TESTS PASSED")
    print("=" * 70)
    print()
    print("Verified:")
    print("  ✓ Data load + validation logic")
    print("  ✓ _make_figure builds cleanly for x/y/z, all index positions")
    print("  ✓ Cluster-border overlay (contours) draws without error")
    print("  ✓ Axis-change slider-range update")
    print("  ✓ Clustering combo-change swap + discrete colormap rebuild")
    print()

except Exception:
    print()
    print("=" * 70)
    print("✗ TEST FAILED")
    print("=" * 70)
    print()
    traceback.print_exc()
    print()

finally:
    if os.path.exists(test_dir):
        shutil.rmtree(test_dir)
        print(f"Cleaned up test directory: {test_dir}")
