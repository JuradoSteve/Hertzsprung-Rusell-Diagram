# Hertzsprung-Rusell-Diagram

This code generate a [Hertzsprung-Rusell diagram](https://en.wikipedia.org/wiki/Hertzsprung%E2%80%93Russell_diagram) from a stellar astrophysics homework based in the text [An Introduction to Modern Astrophysics (2nd Edition) - Bradley W. Carroll & Dale A. Ostile](https://www.amazon.com/Introduction-Modern-Astrophysics-2nd/dp/0805304029).

The homework's taks were:

> The main sequence present an aproximate mass-luminosity relation as <img alt="L \propto M^{7/2}" src="https://render.githubusercontent.com/render/math?math=L%20%5Cpropto%20M%5E%7B7%2F2%7D" style="transform: translateY(20%);" /> and a radius-mass relation as <img alt="R \propto M^{4/5}" src="https://render.githubusercontent.com/render/math?math=R%20%5Cpropto%20M%5E%7B4%2F5%7D" style="transform: translateY(20%);" />.
1. With the before relations you can graph the main sequence in an Hertzsprung-Rusell theoretical diagram (HRD). Your HRD should cover the range 3.5 - 4.5 for
1. <img alt="\log{T_{eff}}" src="https://render.githubusercontent.com/render/math?math=%5Clog%7BT_%7Beff%7D%7D" style="transform: translateY(20%);" /> and a appropiate range for <img alt="\log{L/L_{\odot}}" src="https://render.githubusercontent.com/render/math?math=%5Clog%7BL%2FL_%7B%5Codot%7D%7D" style="transform: translateY(20%);" />. Hint: Derivate first a expresion for <img alt="L" src="https://render.githubusercontent.com/render/math?math=L" style="transform: translateY(20%);" /> in <img alt="T_{eff}" src="https://render.githubusercontent.com/render/math?math=T_%7Beff%7D" style="transform: translateY(20%);" /> terms for stars in main sequences.
We now that the relation between the luminosity and the effective temperature for a star is:

<p align="center"><img alt="L = 4\pi R_{\star}^{2} \sigma T_{eff}^{4}" src="https://render.githubusercontent.com/render/math?math=L%20%3D%204%5Cpi%20R_%7B%5Cstar%7D%20%5Csigma%20T_%7Beff%7D%5E%7B4%7D"/></p>

if we divided with the Sun's values:
$$\frac{L}{L_{\odot}} = \frac{4\pi R_{\star}^{2} \sigma T_{eff}^{4}}{4\pi R_{\odot}^{2} \sigma T_{eff,\odot}^{4}}$$
$$\frac{L}{L_{\odot}} = \frac{R_{\star}^{2}T_{eff}^{4}}{R_{\odot}^{2}T_{eff,\odot}^{4}}$$

from the above relations we have that:
$$\frac{R_{\star}}{R_{\odot}} = \left(\frac{M_{\star}}{M_{\odot}}\right)^{4/5}$$
$$\frac{L_{\star}}{L_{\odot}} = \left(\frac{M_{\star}}{M_{\odot}}\right)^{7/5}$$

for main sequence:
$$\left(\frac{R_{\star}}{R_{\odot}}\right)^{2} = \left(\frac{L_{\star}}{L_{\odot}}\right)^{16/35}$$

$$\frac{L}{L_{\odot}} = \left(\frac{L_{\star}}{L_{\odot}}\right)^{16/35}\frac{T_{eff}^{4}}{T_{eff,\odot}^{4}}$$
$$\left(\frac{L_{\star}}{L_{\odot}}\right)^{19/35} = \frac{T_{eff}^{4}}{T_{eff,\odot}^{4}}$$
$$\log{\left(\frac{L_{\star}}{L_{\odot}}\right)} = \left(\frac{35}{19}\right)4\log{\left(\frac{T_{eff}}{T_{eff,\odot}}\right)}$$




```python

```
