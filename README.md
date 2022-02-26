# Hertzsprung-Rusell-Diagram

This code generate a [Hertzsprung-Rusell diagram](https://en.wikipedia.org/wiki/Hertzsprung%E2%80%93Russell_diagram) from a stellar astrophysics homework based in the text [An Introduction to Modern Astrophysics (2nd Edition) - Bradley W. Carroll & Dale A. Ostile](https://www.amazon.com/Introduction-Modern-Astrophysics-2nd/dp/0805304029).

The homework's taks were:

> The main sequence present an aproximate mass-luminosity relation as <img src="https://latex.codecogs.com/svg.image?L&space;\propto&space;M^{7/5}" title="L \propto M^{7/5}" /> and a radius-mass relation as <img src="https://latex.codecogs.com/svg.image?R&space;\propto&space;M^{4/5}" title="R \propto M^{4/5}"/>.
1. With the before relations you can graph the main sequence in an Hertzsprung-Rusell theoretical diagram (HRD). Your HRD should cover the range 3.5 - 4.5 for
<img src="https://latex.codecogs.com/svg.image?\log{T_{\text{eff}}}" title="\log{T_{\text{eff}}}"/> and a appropiate range for <img src="https://latex.codecogs.com/svg.image?\log{L/L_{\odot}}" title="\log{L/L_{\odot}}"/>. Hint: Derivate first a expresion for <img src="https://latex.codecogs.com/svg.image?L" title="L"/> in <img src="https://latex.codecogs.com/svg.image?T_{\text{eff}}" title="T_{\text{eff}}"/> terms for stars in main sequences.


We now that the relation between the luminosity and the effective temperature for a star is:

<p align="center"><img src="https://latex.codecogs.com/svg.image?L&space;=&space;4&space;\pi&space;R_{\star}&space;\sigma&space;T_{\text{eff}}^{4}" title="L = 4 \pi R_{\star} \sigma T_{\text{eff}}^{4}"/></p>

where <img src="https://latex.codecogs.com/svg.image?\sigma" title="\sigma"/> is the [Stefan-Boltzmann constant](https://en.wikipedia.org/wiki/Stefan%E2%80%93Boltzmann_constant) and <img src="https://latex.codecogs.com/svg.image?R_{\star}" title="R_{\star}"/> is the star's radius.

if we divided with the Sun's values:

<p align="center"><img src="https://latex.codecogs.com/svg.image?\frac{L}{L_{\odot}}&space;=&space;\frac{4\pi&space;R_{\star}^{2}&space;\sigma&space;T_{eff}^{4}}{4\pi&space;R_{\odot}^{2}&space;\sigma&space;T_{eff,\odot}^{4}}" title="\frac{L}{L_{\odot}} = \frac{4\pi R_{\star}^{2} \sigma T_{eff}^{4}}{4\pi R_{\odot}^{2} \sigma T_{eff,\odot}^{4}}"/></p>

<p align="center"><img src="https://latex.codecogs.com/svg.image?\frac{L}{L_{\odot}}&space;=&space;\frac{R_{\star}^{2}T_{eff}^{4}}{R_{\odot}^{2}T_{eff,\odot}^{4}}" title="\frac{L}{L_{\odot}} = \frac{R_{\star}^{2}T_{eff}^{4}}{R_{\odot}^{2}T_{eff,\odot}^{4}}"/></p>

from the above relations we have that:

<p align="center"><img src="https://latex.codecogs.com/svg.image?\frac{R_{\star}}{R_{\odot}}&space;=&space;\left(\frac{M_{\star}}{M_{\odot}}\right)^{4/5}" title="\frac{R_{\star}}{R_{\odot}} = \left(\frac{M_{\star}}{M_{\odot}}\right)^{4/5}"/></p>

<p align="center"><img src="https://latex.codecogs.com/svg.image?\frac{L_{\star}}{L_{\odot}}&space;=&space;\left(\frac{M_{\star}}{M_{\odot}}\right)^{7/5}" title="\frac{L_{\star}}{L_{\odot}} = \left(\frac{M_{\star}}{M_{\odot}}\right)^{7/5}"/></p>

for main sequence:

<p align="center"><img src="https://latex.codecogs.com/svg.image?\left(\frac{R_{\star}}{R_{\odot}}\right)^{2}&space;=&space;\left(\frac{L_{\star}}{L_{\odot}}\right)^{16/35}" title="\left(\frac{R_{\star}}{R_{\odot}}\right)^{2} = \left(\frac{L_{\star}}{L_{\odot}}\right)^{16/35}"/></p>

<p align="center"><img src="https://latex.codecogs.com/svg.image?\frac{L}{L_{\odot}}&space;=&space;\left(\frac{L_{\star}}{L_{\odot}}\right)^{16/35}\frac{T_{eff}^{4}}{T_{eff,\odot}^{4}}" title="\frac{L}{L_{\odot}} = \left(\frac{L_{\star}}{L_{\odot}}\right)^{16/35}\frac{T_{eff}^{4}}{T_{eff,\odot}^{4}}"/></p>

<p align="center"><img src="https://latex.codecogs.com/svg.image?\left(\frac{L_{\star}}{L_{\odot}}\right)^{19/35}&space;=&space;\frac{T_{eff}^{4}}{T_{eff,\odot}^{4}}" title="\left(\frac{L_{\star}}{L_{\odot}}\right)^{19/35} = \frac{T_{eff}^{4}}{T_{eff,\odot}^{4}}"/></p>

<p align="center"><img src="https://latex.codecogs.com/svg.image?\log{\left(\frac{L}{L_{\odot}}\right)}&space;=&space;4\left(\frac{35}{19}\right)\log{\left(\frac{T_{\text{eff}}}{5777}\right)}" title="\log{\left(\frac{L}{L_{\odot}}\right)} = 4\left(\frac{35}{19}\right)\log{\left(\frac{T_{\text{eff}}}{5777}\right)}"/></p>

here i used the effective temperature of sun equal to <img src="https://latex.codecogs.com/svg.image?T_{\text{eff},&space;\odot}&space;=&space;5771&space;\:&space;\text{K}" title="T_{\text{eff}, \odot} = 5771 \: \text{K}"/>

2. Draw a dashed line in constants stelar radius equal to <img src="https://latex.codecogs.com/svg.image?R_{\star}&space;=&space;0.1,&space;1,&space;10,&space;100" title="R_{\star} = 0.1, 1, 10, 100"/>.
3. Betelgeuse star has <img src="https://latex.codecogs.com/svg.image?T_{\text{eff}}&space;=&space;3500&space;\;&space;\text{K}" title="T_{\text{eff}} = 3500 \; \text{K}"/> and <img src="https://latex.codecogs.com/svg.image?L&space;=&space;63000&space;L_{\odot}" title="L = 63000 L_{\odot}"/> . Show the position of this star on your HRD.

At the moment resulting HRD is:


