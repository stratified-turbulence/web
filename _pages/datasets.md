---
layout: splash
title: "Datasets"
permalink: /Datasets/
author_profile: false
---

# Datasets

Datasets, and associated analysis tools, will progressively be added to the tables below. Data are hosted on the <a href="https://doi.ccs.ornl.gov/" target="_blank">Constellation repository</a> and may be downloaded to a local computer using <a href="https://www.globus.org/" target="_blank">Globus</a>. Not all data are currently uploaded to Constellation; please contact the group if you are interested in any datasets that are not yet available. 

Further details about the simulations are provided within the collapsible headings below.


<details>
  <summary class="big-summary"><strong>Equations of motion</strong></summary>

  <div markdown="1">
  
  All direct numerical simulations (DNS) are performed under the following conditions.

  The density field $\rho$ satisfies
  \begin{equation}
  \rho\left(\mathbf{x},t\right)=\rho_{0}+\bar{\rho}\left(z\right)+\rho'\left(\mathbf{x},t\right),\ \ \bar{\rho}\left(z\right)=-Az,
  \end{equation}
  where $z$ is taken to point upward in the opposite direction of gravity, $\rho_0$ denotes a reference density, $A$ is a constant describing the linear background vertical density gradient, and $\rho'$ denotes (turbulent) fluctuations away from the background state.

  The Navier-Stokes equations are then solved under the Boussinesq approximation; specifically, variations in density away from the background reference value $\rho_0$ are assumed to be small and such density variations are thus only accounted for when computing the buoyancy force. The resulting equations of motion that are solved numerically are:
 
  $$
  \begin{align}
  \nabla\cdot\mathbf{u} &= 0, \\ 
 \rho_{0}\left(\frac{\partial\mathbf{u}}{\partial t}+\left(\mathbf{u}\cdot\nabla\right)\mathbf{u}\right)&=-\nabla p'+\mu\nabla^{2}\mathbf{u}-\rho'g\hat{\mathbf{z}}+\mathbf{F}, \\
  \frac{\partial\rho'}{\partial t}+\mathbf{u}\cdot\nabla\rho'+w\frac{\partial\bar{\rho}}{\partial z} &= \kappa\nabla^{2}\rho'.
  \end{align}
  $$

  Equation (2) is the incompressibility condition arising from mass conservation under the Boussinesq approximation, with $\mathbf{u}=\left(u,v,w\right)$ describing the fluid velocity. Equation (3) is the momentum equation, where the pressure field has been decomposed as $p\left(\mathbf{x},t\right)=\bar{p}\left(z\right)+p'\left(\mathbf{x},t\right)$ such that $\partial\bar{p}/\partial z=-\rho_{0}g$ (i.e. $\bar{p}\left(z\right)$ is the hydrostatic pressure arising from the ambient density $\rho_0$). The gravitational acceleration is $g$, the viscosity $\mu$, and $\mathbf{F}$ denotes a body force that is used in some simulations to sustain turbulence in a steady-state (i.e. statistically-stationary turbulence). Equation (4) is an advection-diffusion equation governing density perturbations $\rho'$ away from the linear background stratification, with $\kappa$ denoting the molecular diffusivity.

  A fractional-step pseudospectral method is used to solve equations (2-4) in dimensional form in a three-dimensional box. The variables $\mathbf{u}=\left(u,v,w\right)$ and $\rho'$ all satisfy periodic boundary conditions. Values of the following constants are provided with each dataset in a text file "params.txt":

<div style="max-width: 600px; margin: auto;">
  <table>
    <!-- <thead>
      <tr>
        <th>Column 1</th><th>Column 2</th>
      </tr>
    </thead> -->
    <tbody>
      <tr><td>$L_x, L_y, L_z$</td><td>Box dimensions</td></tr>
      <tr><td>$N_x, N_y, N_z$</td><td>Number of grid points in each dimension</td></tr>
      <tr><td>$g=1$</td><td>Gravitational acceleration (fixed in all cases)</td></tr>
      <tr><td>$\rho_0=1$</td><td>Reference density (fixed in all cases)</td></tr>
      <tr><td>$A = \partial\bar{\rho}/\partial z$</td><td>Background density gradient (a linear gradient is always used)</td></tr>
      <tr><td>$\nu = \mu/\rho_0$</td><td>Kinematic viscosity</td></tr>
      <tr><td>$Pr=\nu/\kappa$</td><td>Prandtl number, ratio of kinematic viscosity to molecular diffusivity</td></tr>
    </tbody>
  </table>
</div>

Note that parameter values need only be chosen such that the dimensionless groups of relevance in characterizing the turbulent flow (i.e. $Re$, $Fr$ etc, described below) emerge to be the desired values. Therefore, it is often simpler to use scaled values of the parameters (such as $g=1$ instead of $g=9.81 \ m/s^2$, for example) when running the simulations. 

<br>


  </div>
</details>

<details>
  <summary class="big-summary"><strong>Relevant dimensionless groups, length scales</strong></summary>

  <div markdown="1">

  The equations of motion (2-4) may be non-dimensionalized using

  \begin{equation}
    \hat{x}=x/L,\ \hat{u}=u/U,\ \hat{t}=t\left(U/L\right),\ \hat{p}=p/\left(\rho_{0}U^{2}\right),\ \hat{\rho}=\rho/\left(\left[d\bar{\rho}/dz\right]L\right),
  \end{equation}
  where hats indicate non-dimensional quantities. The equations of motion in non-dimensional form are then

  $$
  \begin{align}
  \nabla\cdot\hat{\mathbf{u}}&=0, \\ 
  \frac{\partial\hat{\mathbf{u}}}{\partial\hat{t}}+\left(\hat{\mathbf{u}}\cdot\hat{\nabla}\right)\hat{\mathbf{u}}&=-\hat{\nabla}\hat{p}'+\frac{1}{Re}\hat{\nabla^{2}}\hat{\mathbf{u}}-\frac{1}{Fr^{2}}\hat{\rho}'\hat{\mathbf{z}}+\hat{\mathbf{F}}, \\
  \frac{\partial\hat{\rho}'}{\partial\hat{t}}+\hat{\mathbf{u}}\cdot\hat{\nabla}\hat{\rho}'-\hat{w}&=\frac{1}{PrRe}\hat{\nabla}^{2}\hat{\rho}',
  \end{align}
  $$

  where 
  \begin{equation}
  Re=\frac{UL}{\nu},\ \ Fr=\frac{U}{LN},\ \ Pr=\frac{\nu}{\kappa}, \ \ N=\sqrt{-\frac{g}{\rho_{0}}\frac{\partial\bar{\rho}}{\partial z}}.
  \end{equation}

  The three key dimensionless groups that emerge are the Reynolds ($Re$), Froude ($Fr$), and Prandtl ($Pr$) numbers. The parameter $N$ appearing in the Froude number is the buoyancy frequency $N=2\pi f$ charactizing the vertical oscillation frequency $f$ of a parcel of fluid that is perturbed in a local background density gradient $\partial\bar{\rho} / \partial z$. We note that in characterizing our datasets, we typically use a scaled version of the Froude number $Fr=\frac{2\pi U}{NL}$, as it is $f$ (with dimensions of $1/s$) that characterizes the oscillation frequency of the fluid parcel. 
  
  The above dimensionless groups may be combined to form other informative groups, and can be physically interpreted in terms of ratios of length or time scales characterizing the flow, as summarized in the table below.



<div style="max-width: 600px; margin: auto;">
<table>
  <tr>
  <th colspan="2" style="border-bottom: 1px solid #ccc;">Length Scales</th>
  </tr>
  <tr><td>$L$</td><td>Scale of largest eddy</td></tr>
  <tr><td>$L_{0}=\sqrt{\epsilon/N^{3}}$</td><td>Ozmidov length (scale below which buoyancy effects do not play significant role)</td></tr>
  <tr><td>$L_{C}=\sqrt{\epsilon/S^{3}}$</td><td>Corrsin length (if background vertical shear $S\equiv \partial u/\partial z$ is significant, scale below which shear does not play significant role)</td></tr>
  <tr><td>$L_{K}=\left(\nu^{3}/\epsilon\right)^{\frac{1}{4}}$</td><td>Kolmogorov length (scale at which kinetic energy is dissipated by viscosity)</td></tr>
  <tr><td>$L_{B}=L_{K}/\sqrt{Pr}$</td><td>Batchelor length (scale at which density fluctuations are dissipated)</td></tr>
  <tr><td colspan="2" style="border: none; height: 10px;"></td></tr>
  <tr>
  <th colspan="2" style="border-bottom: 1px solid #ccc;">Dimensionless Groups</th>
  </tr>
  <tr><td>$Re=\frac{UL}{\nu}$</td><td>Controls separation between largest and smallest length scales in flow, with $L_B$ then controlling scales below $L_K$; $L/L_{K}=Re^{\frac{3}{4}}$ (assuming $\epsilon=U^{3}/L$) </td></tr>
  <tr><td>$Fr=\frac{U}{LN}$</td><td>Influence of stratification. Controls length scales influenced by buoyancy; $L_{O}/L=Fr^{\frac{3}{2}}$</td></tr>
  <tr><td>$Re_b = \epsilon / (\nu N^2)$</td><td>Reynolds buoyancy number. Controls extent of inertial range uninfluenced by buoyancy; $L_{O}/L_{K}=Re_{b}^{\frac{3}{4}}$. Note $Re_{b}=ReFr^{2}$ assuming $\epsilon=U^{3}/L$</td></tr>
  <tr><td>$Pr=\frac{\nu}{\kappa}$</td><td>Prandtl number. Controls separation between dissipation scales of velocity and density fluctuations; $L_{K}/L_{B}=\sqrt{Pr}$</td></tr>
</table>
</div>

The figure below illustrates the range of relevant length scales that must be resolved in a DNS of stratified turbulence.

<div style="text-align: center;">
  <img src="/web/images/lengthScales.jpg" alt="Alt text" style="width: 700px;">
</div>

<br>

 
  </div>
</details>


<details>
<summary class="big-summary"><strong>Data formatting</strong></summary>

<div markdown="1">

Simulation outputs are stored as binary files of the form "{var}.{#}", where {var}={u,v,w,r} corresponds to the three velocity components $(u,v,w)$ and the perturbed density field $\rho'$ away from the background density gradient. The {#} corrsponds to the timestamp of the simulation, which may be converted into a physical time based on the reported timestep. 

The three-dimensional grid for a given variable and timestep is stored as a one-dimensional string of single-precision numbers in order of $x$ (fastest changing index), $y$, $z$ (slowest changing index). To easily detect errors in reading and reshaping the raw data into a three-dimensional grid, two zeros are padded onto the end of the $x$-dimension. The datafiles thus have size $\left(N_{x}+2\right)\times N_{y}\times N_{z}$. Python codes are provided to read and save a given binary file as a three-dimensional array (e.g. as a NumPy array). For larger datasets, it is advisable to use a <a href="https://numpy.org/doc/stable/reference/generated/numpy.memmap.html" target="_blank">memory map</a> which allows one to easily extract slices of the fields without loading the entire three-dimensional array into memory.

</div>
</details>


<!-- ## Equations of motion {#equations-of-motion}
All DNS are characterized as follows.

The density field obeys

$$
\begin{equation*}
\rho\left(\mathbf{x},t\right)=\rho_{0}+\bar{\rho}\left(z\right)+\rho'\left(\mathbf{x},t\right),\ \ \bar{\rho}\left(z\right)=-Az,
\end{equation*}
$$

as is characterized by a uniform background density gradient.

The equations of motion solved are:

$$
\begin{align*}
\nabla\cdot\mathbf{u} &= 0, \\ 
\rho_{0}\left(\frac{\partial\mathbf{u}}{\partial t}+\left(\mathbf{u}\cdot\nabla\right)\mathbf{u}\right) &= -\nabla p'+\mu\nabla^{2}\mathbf{u}-\rho'g\hat{\mathbf{z}} \\
\frac{\partial\rho'}{\partial t}+\mathbf{u}\cdot\nabla\rho'+w\frac{\partial\bar{\rho}}{\partial z} &= \kappa\nabla^{2}\rho'
\end{align*}
$$

Here, we have decomposed the pressure as $p\left(\mathbf{x},t\right)=\bar{p}\left(z\right)+p'\left(\mathbf{x},t\right),\ \ \frac{\partial p_{0}}{\partial z}=-\rho_{0}g$. -->


<!-- ## General guidelines on data formatting {#general-guidelines-on-data-formatting}
Binary files are provided for the following primitive variables:
- Three-dimensional fields of the velocity components $\left(u,v,w\right)$
- Perturbation density field $\rho'$ with respect to background gradient

Files are stored on the [Constellation repository](https://doi.ccs.ornl.gov/), which may be downloaded to your local computer/server via [Globus](https://www.globus.org/). 

The numerical precision (single or double) of the saved data is specified, and varies between datasets. To easily detect errors in reading and reshaping the raw data, two zeros are padded onto the end of the $x$-dimension. The datafiles thus have size $\left(N_{x}+2\right)\times N_{y}\times N_{z}$. Python code is provided to read and save a given binary file as a three-dimensional array (e.g. as a NumPy array). For the larger datasets, it is advisable to use a memory map to avoid overloading your local RAM.  -->


## Database {#datasets}

DNS runs may be broadly categorized as follows, with further details and download links (if available) provided in the following tables:

- **Time-independent (statistically-stationary) --** A single snapshot of the steady turbulent flow (dissipation balanced by forcing) is provided for a given set of parameters. Turbulence is maintained via the following body forcing schemes:
    - **A. Forced, no mean shear:** Large spectral modes forced, without introducing mean shear, so as to maintain prescribed energy spectrum at large scales.
        - Methodology: <a href="https://doi.org/10.1080/14685248.2012.702909" target="_blank">Almalkie and de Bruyn Kops, *JoT*, 2012</a> 
    - **B. Forced, vertical shear:** Background vertical shear injects energy; Richardson number varied to maintain fixed kinetic energy.
        - Methodology: <a href="https://doi.org/10.1103/PhysRevLett.122.194504" target="_blank">Portwood, de Bruyn Kops, and Caulfield, *PRL*, 2019</a> <br><br>


- **Time-dependent evolution.** Turbulence initialized using initial flow fields described below, then allowed to freely evolve without forcing. Multiple flow snapshots saved over time.
    - **C. Decaying, initially unstratified:** Field of unstratified turbulence generated, gravitational force is then introduced, flow is observed over time as it decays.
        - Methodology: <a href="https://doi.org/10.1017/jfm.2018.888" target="_blank">de Bruyn Kops and Riley, *JFM*, 2018</a> 

    - **D. Taylor-Green vortices:** Turbulence triggered by initially laminar field of Taylor-Green vortices, develops, and then decays back to laminar state.
        - Methodology: <a href="https://doi.org/10.1063/1.1578077" target="_blank">Riley and de Bruyn Kops, *PoF*, 2003</a> 


Once downloaded, data may be accessed using scripts provided <a href="https://github.com/muralikrishnangm/getData-SST.git" target="_blank">in this Github Respository</a>, which includes Python scripts for extracting subdomains and visualizing snapshots.


<div style="border: 2px solid #ccc; padding: 1.5em; border-radius: 12px; margin: 3em 0;">
  <!-- Two-column section -->
  <div style="display: flex; align-items: center; justify-content: space-between; gap: 2em;">
    <div style="flex: 1;">
      <h2 style="margin-top: 0;"> Taylor-Green</h2> 

<div markdown="1">
  - Three datasets spanning $Pr=\nu/\kappa=\left[1,7,50\right]$
  - Fixed $Fr=2\pi U/\left(NL\right)=4$, $Re=UL/\nu=3200$
</div>

      <p><a href="/web/portfolio/taylorgreen/" style="color: #007acc; font-weight: bold;">Video, further details →</a></p>

    </div>
    
    <div style="flex: 1;">
      <img src="/web/images/TG.jpg" alt="Taylor-Green" style="width: 100%; border: none;">
    </div>
  </div>

  <!-- Full-width section -->
  <div style="margin-top: 2em;">

  <div markdown="1">

  

  | Name, dataset link, parameter file | $Pr$   |   Number of snapshots in time  |  Grid points $(N_x=N_y, N_z)$ | Field size (per variable, snapshot) | Total dataset size
  | --------           | ------ | ------|        |
  | <a href="https://doi.org/10.13139/OLCF/2530508" target="_blank">TG_P1F4R32</a>   | 1     | 15,000 | $512^2 \times 256$ |255 MB| 15 GB
  | TG_P7F4R32 (upload in progress)   | 7     | 15,250  | $1280^2 \times 640$ | 4 GB| 244 TB
  | TG_P50F4R32 (upload in progress)   |  50     | 1,680  | $3584^2 \times 1792$ | 86 GB  | 577 TB

  </div>
  </div>
</div>




<div style="border: 2px solid #ccc; padding: 1.5em; border-radius: 12px; margin: 3em 0;">
  <!-- Two-column section -->
  <div style="display: flex; align-items: center; justify-content: space-between; gap: 2em;">
    <div style="flex: 1;">
      <h2 style="margin-top: 0;">Forced, no mean shear</h2>
      
<div markdown="1">
- Nine datasets spanning $Pr=\nu/\kappa=\left[1,7,50\right]$ and $Fr=2\pi U/\left(NL\right)=\left[0.5,1,2\right]$
- Fixed $Re_b \approx 50$
</div>

      <!-- <p> Three datasets spanning Prandtl numbers $Pr={1,7,50}$ with fixed Froude $Fr=4/(2 \pi) \approx 0.64$ and Reynolds $Re=3200$ numbers.</p>
      <p><a href="/web/portfolio/taylorgreen/" style="color: #007acc; font-weight: bold;">Video and further details →</a></p> -->
    </div>
    <div style="flex: 1;">
      <img src="/web/images/Forced.jpg" alt="Taylor-Green" style="width: 100%; border: none;">
    </div>
  </div>

  <!-- Full-width section -->
  <div style="margin-top: 2em;">

  <div markdown="1">

  Data not currently uploaded to Constellation. Please contact group for access.


  |Name, dataset link, parameter file | $Pr$ |  $Fr_h$ | Grid points $(N_x=N_y, N_z)$ | Field size (per variable, snapshot) 
  | --------          | ------ | ------|        |
  | F_P1F050Gn50    | 1     | 0.5  | $8192^2 \times 1024$  | 275 GB|
  | F_P1F100Gn50    | 1     | 1  | $4096^2 \times 4096$  | 275 GB|
  | F_P1F200Gn50    | 1     | 2   | $2048^2 \times 1024$  | 17 GB| 
  | F_P7F050Gn50    | 7     | 0.5   | $30240^2 \times 3780$ | 13.8 TB |
  | F_P7F100Gn50    | 7     | 1   | $8192^2 \times 2048$  | 550 GB|
  | F_P7F200Gn50    | 7     | 2   | $6144^2 \times 3072$  | 464 GB | 
  | F_P50F050Gn50   | 50    | 0.5   | $37632^2 \times 4704$ |26.6 TB|
  | F_P50F100Gn50   | 50    | 1   | $28672^2 \times 7168$ |23.6 TB|
  | F_P50F200Gn50   | 50    | 2   | $8192^2 \times 4096$  |1.01 TB|

  </div>
  </div>
</div>



<div style="border: 2px solid #ccc; padding: 1.5em; border-radius: 12px; margin: 3em 0;">
  <!-- Two-column section -->
  <div style="display: flex; align-items: center; justify-content: space-between; gap: 2em;">
    <div style="flex: 1;">
      <h2 style="margin-top: 0;">Forced, vertical shear</h2>
<div markdown="1">
- Fifteen datasets spannin three $Pr=\nu/\kappa=\left[1,7,50\right]$ and five buoyancy Reynolds numbers $(Re_b)=[30,1000]$
- Fixed Richardson number $Ri\approx 0.15$

</div>
      <!-- <p> Three datasets spanning Prandtl numbers $Pr={1,7,50}$ with fixed Froude $Fr=4/(2 \pi) \approx 0.64$ and Reynolds $Re=3200$ numbers.</p>
      <p><a href="/web/portfolio/taylorgreen/" style="color: #007acc; font-weight: bold;">Video and further details →</a></p> -->
    </div>
    <div style="flex: 1;">
      <img src="/web/images/sheared.jpg" alt="Taylor-Green" style="width: 100%; border: none;">
    </div>
  </div>

  <!-- Full-width section -->
  <div style="margin-top: 2em;">

  <div markdown="1">

  Data not currently uploaded to Constellation. Please contact group for access.

  | Name and dataset link | $Pr$ |  $Gn$ | Grid points $(N_x, N_y, N_z)$ | Field size (per variable, snapshot) |
  | --------           | ------ | ------|        |
  | S_P1Gn30    | 1     | 34.7 |  $1536 \times 768 \times 384$ |
  | S_P7Gn30    | 7     | 33.9 |  $3072 \times 1536 \times 768$ |
  | S_P50Gn30   | 50    | 35.5 |  $2560 \times 1280 \times 640$ |
  | S_P1Gn80    | 1     | 81.1 |  (in progress)
  | S_P7Gn80    | 7     | 83.0 |  $5120 \times 2560 \times 1280$ |
  | S_P50Gn80   | 50    | 83.9 |  $8192 \times 4096 \times 2048$ |
  | S_P1Gn200   | 1     | 210 |   $1536 \times 768 \times 384$ |
  | S_P7Gn200   | 7     | 207 |   $8192 \times 4096 \times 2048$ |
  | S_P50Gn200  | 50    | 206 |   (in progress)
  | S_P1Gn600   | 1     | 687 |   $7168 \times 3584 \times 1792$ |
  | S_P7Gn600   | 7     | 528 |   $23040 \times 11520 \times 5760$ |
  | S_P50Gn600   | 50    |  | (planned run)
  | S_P1Gn1000  | 1     | 1013|  $7168 \times 3584 \times 1792$ |
  | S_P7Gn1000  | 7     | 821 |  $31680 \times 15840 \times 7920$ |
  | S_P50Gn1000   | 50    |  | (planned run)

  </div>
  </div>
</div>


<div style="border: 2px solid #ccc; padding: 1.5em; border-radius: 12px; margin: 3em 0;">
  <!-- Two-column section -->
  <div style="display: flex; align-items: center; justify-content: space-between; gap: 2em;">
    <div style="flex: 1;">
      <h2 style="margin-top: 0;">Decaying, initially unstratified</h2>
      <!-- <p> Three datasets spanning Prandtl numbers $Pr={1,7,50}$ with fixed Froude $Fr=4/(2 \pi) \approx 0.64$ and Reynolds $Re=3200$ numbers.</p>
      <p><a href="/web/portfolio/taylorgreen/" style="color: #007acc; font-weight: bold;">Video and further details →</a></p> -->
      (Details coming soon)
    </div>
    <div style="flex: 1;">
      <!-- <img src="/web/images/Decaying.png" alt="Taylor-Green" style="width: 100%; border: none;"> -->
    </div>
  </div>

  <!-- Full-width section -->
  <div style="margin-top: 2em;">

  <div markdown="1">

  

  </div>
  </div>
</div>


<!-- ## Test Plots

<iframe src="/web/assets/plots/plot.html" 
        width="100%" 
        height="600px" 
        style="border: none;"></iframe> -->


