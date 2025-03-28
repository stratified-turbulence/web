---
layout: splash
title: "Datasets"
permalink: /Datasets/
author_profile: false
---

# Datasets and Code

Datasets (and associated analysis codes) will progressively be added to this page. Some data may be listed below without a direct link to a database; in this case, please contact the group if you would like access to the data. 


## General guidelines on data formatting
Binary files are provided for the following primitive variables:
- Three-dimensional fields of the velocity components $\left(u,v,w\right)$
- Perturbation density field $\rho'$ with respect to background gradient

Files are stored on the [Constellation repository](https://doi.ccs.ornl.gov/), which may be downloaded to your local computer/server via [Globus](https://www.globus.org/). 

The numerical precision (single or double) of the saved data is specified, and varies between datasets. To easily detect errors in reading and reshaping the raw data, two zeros are padded onto the end of the $x$-dimension. The datafiles thus have size $\left(N_{x}+2\right)\times N_{y}\times N_{z}$. Python code is provided to read and save a given binary file as a three-dimensional array (e.g. as a NumPy array). For the larger datasets, it is advisable to use a memory map to avoid overloading your local RAM. 

## Equations of motion 
To be updated.


## Time-evolving flows

* ### Taylor-Green

    Three datasets spanning a variety of Prandtl numbers $Pr={1,7,50}$ with fixed Froude $(Fr)$ and Reynolds $(Re)$ numbers.

    The $Pr=1$ dataset was originally reported by [Riley and de Bruyn Kops, PoF, 2003](https://pubs.aip.org/aip/pof/article-abstract/15/7/2047/255008/Dynamics-of-turbulence-strongly-influenced-by?redirectedFrom=fulltext). Through the INCITE program, these data have recently been extended to $Pr=7,50$, as reported in the analysis of [Petropoulous et al, JFM, 2025](https://www.cambridge.org/core/journals/journal-of-fluid-mechanics/article/modelling-dispersion-in-stratified-turbulent-flows-as-a-resetting-process/C9D566B4ABF95A35883CE4B213D947A9)

    | Name and dataset link      | $Pr$   |   Number of snapshots  | Field size (per snapshot)                                      |
    | --------           | ------ | ------|        |
    | [TG_P1F4R32](#)    | 1     | 15,000 | 255 MB|
    | [TG_P7F4R32](#)    | 7     | 27,000  | 3.9 GB|
    | [TG_P50F4R32](#)   |  50     | 1,680   | 84 GB  | 




<!-- * ## Steady-state

    * ### Vortically-forced

        Description and summary of data

        | Entry            | Item   |                                                              |
        | --------         | ------ | ------------------------------------------------------------ |
        | [John Doe](#)    | 2016   | Description of the item in the list                          |
        | [Jane Doe](#)    | 2019   | Description of the item in the list                          |
        | [Doe Doe](#)     | 2022   | Description of the item in the list                          |

    * ### Shear-driven

        Description and summary of data

        | Entry            | Item   |                                                              |
        | --------         | ------ | ------------------------------------------------------------ |
        | [John Doe](#)    | 2016   | Description of the item in the list                          |
        | [Jane Doe](#)    | 2019   | Description of the item in the list                          |
        | [Doe Doe](#)     | 2022   | Description of the item in the list                          | -->


## Test Plots

<iframe src="/web/assets/plots/plot.html" 
        width="100%" 
        height="600px" 
        style="border: none;"></iframe>


