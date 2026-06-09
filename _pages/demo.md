---
layout: splash
title: "Code+Demos"
permalink: /Demos/
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
  .gh-repo-card {
    display: inline-block;
    border: 1px solid #d0d7de;
    border-radius: 8px;
    padding: 1rem 1.25rem;
    background: #fff;
    max-width: 420px;
    margin-top: 0.75rem;
    transition: border-color 0.2s, box-shadow 0.2s;
  }
  .gh-repo-card:hover {
    border-color: #0969da;
    box-shadow: 0 2px 8px rgba(0,0,0,0.08);
  }
  .gh-repo-card a {
    display: flex;
    align-items: center;
    gap: 1rem;
    text-decoration: none;
    color: inherit;
  }
  .gh-repo-card a:hover { text-decoration: none; }
  .gh-repo-card svg {
    flex-shrink: 0;
    color: #57606a;
  }
  .gh-repo-card-text .gh-repo-name {
    font-weight: 600;
    font-size: 0.95rem;
    color: #0969da;
    display: block;
  }
  .gh-repo-card-text .gh-repo-desc {
    font-size: 0.82rem;
    color: #57606a;
    margin-top: 0.2rem;
    display: block;
  }
</style>

<div class="demo-prereq">
   To access data on Constellation, a free <a href="https://www.globus.org/" target="_blank">Globus account</a> is required. You can sign up with an existing Google or institutional account.
</div>

## 1. (Quick start) Download and interactively visualize a snapshot in time

This interactive demo runs entirely in Google Colab, no local installation is required. It walks you through authenticating with Globus, downloading one snapshot from the [SST-TG-P1F4R3200](https://doi.ccs.ornl.gov/dataset/5be73ed1-f138-504e-9851-4dff0f465a1d) dataset archived on Constellation (Taylor-Green: Pr = 1, Fr = 4, Re = 3200), and visualizing the downloaded files using Matplotlib in a Jupyter notebook.

<div class="demo-colab-btn">
  <a href="https://colab.research.google.com/github/stratified-turbulence/web/blob/master/download_data.ipynb" target="_blank">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open demo in Colab" style="height: 32px;">
  </a>
</div>

## 2. Interactive field visualization with clustering and overlays

Explore flow segmentation based on the local prevalence of density overturning, following Portwood et al, JFM, 2016. Select different clustering parameters, slice through 3D fields (density, dissipation of kinetic energy, scalar variance), and overlay clustering boundaries. All computations happens in Colab, no local setup required.

<!-- <div class="demo-colab-btn">
  <a href="https://colab.research.google.com/github/stratified-turbulence/web/blob/master/voila_viewer_v2_colab.ipynb" target="_blank">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open demo in Colab" style="height: 32px;">
  </a>
</div> -->

## 3. Useful repositories for local analysis
If downloading data to a local machine, the following respositories provide useful Python scripts for loading and analysis
<div class="gh-repo-card">
  <a href="https://github.com/muralikrishnangm/getData-SST" target="_blank">
    <svg xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24" fill="currentColor"><path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0 0 24 12c0-6.63-5.37-12-12-12z"/></svg>
    <div class="gh-repo-card-text">
      <span class="gh-repo-name">getData-SST</span>
      <span class="gh-repo-desc">Python scripts for extracting subdomains and visualizing snapshots from the STRATA database</span>
    </div>
  </a>
</div>

## More coming soon...



