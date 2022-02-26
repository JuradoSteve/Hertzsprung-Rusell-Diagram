#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 19:13:47 2022

@author: steve
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as tck

star_data = pd.read_csv('./gappendix_mainsequence_carrol.csv',sep=',',
                        header=0)
TSUN = 5771 # Kelvin

log_teff   = np.linspace(3.5,4.5,25)
log_LLSUN = (35/19)*4*(log_teff-np.log10(TSUN))

Rstar = (0.1,1,10,100) # R_SUN
log_LR = lambda Rstar: 2*np.log10(Rstar)+4*(log_teff-np.log10(TSUN))

fig, ax = plt.subplots()
ax.plot(log_teff,log_LLSUN,color='black',markersize=4,alpha=0.7)

for r in Rstar:
    ax.plot(log_teff,log_LR(r),color='gray',
            linestyle='dashed')
    
ax.text(log_teff[-2],log_LR(Rstar[0])[-8],'R = '+'{}'.format(Rstar[0])+'$R_{\odot}$')
ax.text(log_teff[-2],log_LR(Rstar[1])[-8],'R = '+'{}'.format(Rstar[1])+'$R_{\odot}$')
ax.text(log_teff[7],log_LR(Rstar[2])[8],'R = '+'{}'.format(Rstar[2])+'$R_{\odot}$')
ax.text(log_teff[7],log_LR(Rstar[3])[8],'R = '+'{}'.format(Rstar[3])+'$R_{\odot}$')

ax.scatter(np.log10(star_data['t_eff']),np.log10(star_data['lum_lsun']))
ax.plot(np.log10(5771),0,'y*', label='Sun',markersize=10)
ax.plot(np.log10(3500),np.log10(63000),'r*',markersize=10,label='Betelgeuse')
ax.tick_params(axis='both',which='both',direction='in')
ax.yaxis.set_minor_locator(tck.AutoMinorLocator())
ax.xaxis.set_minor_locator(tck.AutoMinorLocator())
ax.legend(frameon=False,loc='lower left')
ax.set_xlim(4.5,3.5) 
ax.set_xlabel(r'$\log{T_{eff}}$')
ax.set_ylabel(r'$\log{L/L_{\odot}}$')

plt.savefig('HDR.png',dpi=300,bbox_inches='tight')
