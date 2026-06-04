# STRATA Demo Notebook — Context Summary

This document summarises everything needed to integrate the demo Jupyter notebook into the STRATA website.

---

## What the notebook does

`download_data.ipynb` is a Google Colab notebook that:
1. Authenticates the user with Globus (free account required)
2. Downloads one time step of the SST-TG-P1F4R3200 dataset from the ORNL Constellation repository
3. Loads the binary data into NumPy arrays, ready for analysis/visualisation

---

## Globus configuration

| Field | Value |
|---|---|
| **Native App Client ID** | `d47db6dc-0428-4076-9a6e-31927d7c7704` |
| **Collection ID** | `57618e0a-2c99-45ff-9694-24141b92fa17` |
| **HTTPS base URL** | `https://g-e320e6.63720f.75bc.data.globus.org` |
| **Collection path** | `/gen101/world-shared/doi-data/OLCF/202504/10.13139_OLCF_2530508` |

The Client ID belongs to a Globus Native App registered under the STRATA Globus account. It is safe to embed publicly in the notebook — it identifies the app, not the user.

---

## Dataset details

**Dataset:** SST-TG-P1F4R3200  
**DOI:** [10.13139/OLCF/2530508](https://doi.ccs.ornl.gov/dataset/5be73ed1-f138-504e-9851-4dff0f465a1d)  
**Description:** Decaying stably-stratified turbulence, Taylor-Green vortex initialisation, Pr = 1, Fr = 4, Re = 3200  
**Total snapshots:** 15,000  
**Grid:** 512 × 512 × 256  

### Variable file names
| File | Description |
|---|---|
| `u1.{timestep}` | x-velocity |
| `u2.{timestep}` | y-velocity |
| `u3.{timestep}` | z-velocity |
| `r.{timestep}` | Perturbed density |

### Binary file format
- 32-bit little-endian floats (`<f4`)
- x varies fastest, z slowest
- x-dimension padded to `Nx + 2 = 514` (two trailing zeros — strip on load)
- Final array shape after loading: `(Nz, Ny, Nx)` = `(256, 512, 512)`

```python
import numpy as np
Nx, Ny, Nz = 512, 512, 256
field = np.fromfile("u1.1002", dtype="<f4").reshape(Nz, Ny, Nx + 2)[:, :, :Nx]
```

### Subdirectory structure
Files are grouped into subdirectories of 1000 time steps:

| Directory | Time steps |
|---|---|
| `01_1to1000` | 1 – 1000 |
| `02_1001to2000` | 1001 – 2000 |
| `03_2001to3000` | 2001 – 3000 |
| … | … |

Formula to compute subdirectory from time step `t`:
```python
idx   = (t - 1) // 1000 + 1
start = (idx - 1) * 1000 + 1
end   = idx * 1000
subdir = f"{idx:02d}_{start}to{end}"
```

---

## Hosting the notebook

The notebook should live in a **public GitHub repository**. Once pushed, the shareable Colab link is:

```
https://colab.research.google.com/github/{org}/{repo}/blob/main/download_data.ipynb
```

### "Open in Colab" badge (for the website)
```markdown
[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/{org}/{repo}/blob/main/download_data.ipynb)
```

### Embedding on a Jekyll/AcademicPages site
Add the badge as a markdown link on the relevant Datasets page, or convert the notebook to HTML (`jupyter nbconvert --to html download_data.ipynb`) and host it as a static page alongside the badge.

---

## User requirements
- A free [Globus account](https://www.globus.org/) (can sign in with Google or institutional credentials)
- No local software installation — runs entirely in Google Colab
