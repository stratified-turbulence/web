---
title: " "
layout: splash
permalink: /
hidden: true
---

<style>
  /* ── Hero ── */
  .hero {
    display: flex;
    align-items: center;
    gap: 2.5rem;
    padding: 2.5rem 0 2rem 0;
    margin-bottom: 1rem;
    border-bottom: 1px solid #e8e8e8;
  }
  .hero-text {
    flex: 1;
    min-width: 0;
  }
  .hero-title {
    font-size: clamp(2rem, 4vw, 3.2rem);
    font-weight: 700;
    margin: 0 0 0.5rem 0;
    line-height: 1.1;
    color: #222;
    letter-spacing: 0.03em;
  }
  .hero-title span { color: #fe5f55; }
  .hero-subtitle {
    font-size: clamp(0.85rem, 1.5vw, 1rem);
    color: #555;
    font-weight: 700;
    line-height: 1.6;
    margin: 0;
    max-width: 420px;
  }
  .hero-video-wrap {
    flex: 1;
    min-width: 0;
    border-radius: 8px;
    overflow: hidden;
    box-shadow: 0 4px 20px rgba(0,0,0,0.2);
  }
  .hero-video-wrap video {
    width: 100%;
    display: block;
  }
  @media (max-width: 650px) {
    .hero { flex-direction: column; }
  }

  /* ── Feature cards ── */
  .feature-cards {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 1.5rem;
    margin: 2.5rem 0 2rem 0;
  }
  .feature-card {
    border-radius: 8px;
    overflow: hidden;
    box-shadow: 0 2px 10px rgba(0,0,0,0.12);
    text-decoration: none !important;
    color: inherit;
    display: block;
    transition: transform 0.2s ease, box-shadow 0.2s ease;
  }
  .feature-card * {
    text-decoration: none !important;
  }
  .feature-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 8px 24px rgba(0,0,0,0.18);
    text-decoration: none;
    color: inherit;
  }
  .feature-card img {
    width: 100%;
    height: 180px;
    object-fit: cover;
    display: block;
  }
  .feature-card-body {
    padding: 1rem 1.25rem 1.25rem;
  }
  .feature-card-body h3 {
    margin: 0 0 0.4rem 0;
    font-size: 1.05rem;
    color: #222;
    text-decoration: none;
  }
  .feature-card-body p {
    font-size: 0.85rem;
    color: #555;
    margin: 0 0 0.75rem 0;
    line-height: 1.5;
    text-decoration: none;
  }
  .feature-card-btn {
    display: inline-block;
    font-size: 0.78rem;
    padding: 0.25rem 0.7rem;
    border: 1px solid #555;
    border-radius: 4px;
    color: #555;
    transition: background 0.2s, color 0.2s;
  }
  .feature-card:hover .feature-card-btn {
    background: #333;
    color: #fff;
    border-color: #333;
  }
  @media (max-width: 650px) {
    .feature-cards { grid-template-columns: 1fr; }
  }
</style>

<!-- ── Hero ── -->
<div class="hero">
  <div class="hero-text">
    <h1 class="hero-title"><span>STRATA</span></h1>
    <p class="hero-subtitle">
      Supercomputing for Stratified Turbulence Research Advancing Theory and Application
    </p>
     <p style="color: #999; font-style: italic; font-size: 0.85rem;">
      Website is currently being updated...
     </p>
  </div>
  <div class="hero-video-wrap">
    <video autoplay muted loop playsinline poster="{{ site.baseurl }}/images/TG.jpg">
      <source src="{{ site.baseurl }}/images/startVis.webm" type="video/webm">
    <source src="{{ site.baseurl }}/images/TG.mp4" type="video/mp4">
    </video>
  </div>
</div>

<!-- ── Feature cards ── -->
<div class="feature-cards">

  <a href="{{ site.baseurl }}/Datasets/" class="feature-card">
    <img src="{{ site.baseurl }}/images/TG.jpg" alt="Datasets">
    <div class="feature-card-body">
      <h3>Datasets</h3>
      <p>Petabyte-scale DNS database of stratified turbulence, spanning a broad range of forcing schemes and parameters.</p>
      <span class="feature-card-btn">Explore →</span>
    </div>
  </a>

  <a href="{{ site.baseurl }}/Gallery/" class="feature-card">
    <img src="{{ site.baseurl }}/images/sheared.jpg" alt="Gallery">
    <div class="feature-card-body">
      <h3>Gallery</h3>
      <p>Visualizations and still images from various datasets.</p>
      <span class="feature-card-btn">View →</span>
    </div>
  </a>

  <a href="{{ site.baseurl }}/Publications/" class="feature-card">
    <img src="{{ site.baseurl }}/images/Forced.jpg" alt="Publications">
    <div class="feature-card-body">
      <h3>Publications</h3>
      <p>Journal articles and conference papers.</p>
      <span class="feature-card-btn">Read →</span>
    </div>
  </a>

</div>

<!-- ── Main content ── -->

## Current Research Themes
The objective of this group is to generate and analyze fully-resolved direct numerical simulations of stratified turbulence, across a variety of flow configurations and parameters, in order to better understand fundamental turbulent processes influenced by buoyancy and their importance to geophysical, industrial, and environmental applications.

- Exascale computing to resolve stratified turbulent flows in previously-inaccessible regions of parameter space
- Probing coupling between large and small-scale flow features to inform reduced-order modelling
- Development of data-driven and machine-learning techniques to extract physical insight from petabyte-scale datasets

<!-- ## Datasets
We are developing a [database of stratified turbulence simulations](https://stratified-turbulence.github.io/web/Datasets/), and associated codes for analysis. Our data spans a variety of:
- **Flow conditions**:
  - Steady-state synthetically-forced or shear-driven;
  - Unforced time-evolution, initialized via unstratified turbulence or Taylor-Green vortices
- **Parameters**:
  - Buoyancy-Reynolds ($Re_b$), Froude ($Fr$), Prandtl ($Pr$), Richardson ($Ri$) numbers -->

## People
This work is collaborative across multiple international institutions, including:

* University of Massachusetts Amherst (US): [Steve de Bruyn Kops](https://www.umass.edu/engineering/about/directory/stephen-de-bruyn-kops)
* Duke University (US): [Andrew Bragg](https://cee.duke.edu/people/andrew-bragg/)
* Princeton University (US): [Paul Yi](https://tune.cee.princeton.edu/people/young-paul-yi/)
* Oak Ridge National Laboratory (US): [Murali Gopalakrishnan Meena](https://www.ornl.gov/staff-profile/murali-gopalakrishnan-meena), [Wes Brewer](https://www.ornl.gov/staff-profile/wesley-h-brewer), [Aditya Kashi](https://www.ornl.gov/staff-profile/aditya-kashi), [Isaac Lyngass](https://www.ornl.gov/staff-profile/isaac-r-lyngaas), [Pei Zhang](https://www.ornl.gov/staff-profile/pei-zhang)
* Imperial College London (UK): [Adrien Lefauve](https://www.alefauve.com/)
* York University (Canada): [Miles Couchman](https://www.yorku.ca/professor/couchman/)

Groups interested in collaboration are encouraged to reach out.

## Funding

We gratefully acknowledge support from:
- [INCITE Leadership Computing Program](https://doeleadershipcomputing.org) (U.S. Department of Energy)
- [High Performance Computing Modernization Program](https://www.hpc.mil/) (U.S. Department of Defense)
- [Natural Sciences and Engineering Research Council of Canada](https://nserc-crsng.canada.ca/en)

<div style="text-align: center; margin-top: 2rem;">
  <img src="/web/images/Logos.jpg" alt="Supporting institutions" style="width: 800px; max-width: 100%;">
</div>
