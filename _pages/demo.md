---
layout: splash
title: "Demo"
permalink: /Demo/
author_profile: false
---

<style>
  .demo-colab-btn {
    display: inline-block;
    margin: 1rem 0 2rem 0;
  }
  .demo-section {
    margin-bottom: 2rem;
  }
  .demo-section h2 {
    border-bottom: 2px solid #e0e0e0;
    padding-bottom: 0.4rem;
    margin-bottom: 1rem;
    font-size: 1.25rem;
  }
  .demo-prereq {
    background: #f8f8f8;
    border-left: 4px solid #fe5f55;
    padding: 0.75rem 1rem;
    border-radius: 0 6px 6px 0;
    margin-bottom: 1.5rem;
    font-size: 0.9rem;
  }
</style>

## Download and Load a Dataset Snapshot

This interactive demo runs entirely in Google Colab — no local installation required. It walks through authenticating with Globus, downloading one snapshot from the STRATA dataset, and loading the binary fields into NumPy arrays ready for analysis.

<div class="demo-prereq">
  <strong>What you need:</strong> A free <a href="https://www.globus.org/" target="_blank">Globus account</a> — you can sign up with an existing Google or institutional account. No other software installation is required.
</div>

<div class="demo-colab-btn">
  <a href="https://colab.research.google.com/github/stratified-turbulence/web/blob/master/download_data.ipynb" target="_blank">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open in Colab" style="height: 32px;">
  </a>
</div>

<div class="demo-section">

## What the notebook does

The notebook walks through four steps:

1. **Install dependencies** — `globus-sdk`, `requests`, `tqdm`
2. **Configure** — choose a time step and variables to download (all settings pre-filled)
3. **Authenticate** — log in via Globus in your browser and paste the authorisation code
4. **Download and load** — retrieves the selected variable files (~255 MB each) and loads them into NumPy arrays

</div>

<div class="demo-section">

## Dataset

**[SST-TG-P1F4R3200](https://doi.ccs.ornl.gov/dataset/5be73ed1-f138-504e-9851-4dff0f465a1d)** — Decaying stably-stratified turbulence, Taylor-green vortex initialisation

| Parameter | Value |
|---|---|
| $Pr$ | 1 |
| $Fr$ | 4 |
| $Re$ | 3200 |
| Grid | $512 \times 512 \times 256$ |
| Snapshots | 15,000 |
| File size | ~255 MB per variable per snapshot |

**Variables:** `u1`, `u2`, `u3` (velocity components), `r` (perturbed density $\rho'$)

</div>

<div class="demo-section">

## Binary file format

Files are 32-bit little-endian floats with x varying fastest. The x-dimension is padded to `Nx + 2 = 514` (two trailing zeros, stripped on load):

```python
import numpy as np
Nx, Ny, Nz = 512, 512, 256
field = np.fromfile("u1.1002", dtype="<f4").reshape(Nz, Ny, Nx + 2)[:, :, :Nx]
# shape: (256, 512, 512)
```

Files are grouped into subdirectories of 1000 time steps (e.g. `02_1001to2000`). The notebook computes the correct subdirectory automatically.

</div>

<div class="demo-section">

## Further details

Full dataset documentation and download links for all STRATA datasets are available on the [Datasets]({{ site.baseurl }}/Datasets/) page.

</div>
