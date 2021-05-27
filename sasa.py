 import numpy as np
    import matplotlib.pyplot as plt\n",
    from scipy.interpolate import CubicSpline\n",
    "#from matplotlib.patches import Ellipse \n",

def L(T, R):
	sig = 5.6704e-8
	return sig*T**4 *4*np.pi*R**2
    
R_sun = 696340e3 # metros
L_sun = 3.827e26 # Watts
R_list = [0.0001*R_sun,0.01*R_sun,R_sun,100*R_sun, 10000*R_sun]

Teff = np.linspace(10**3,10**5, 200)

# Lista de estrellas de la secuencia principal
T_star = np.array([50000,38000,30000,16400,10800,8620,
	                 7240,6540,5920,5780,5610,5240,4410,
                   3800,3120,2650,2200])
L_star = np.array([800000,180000,20000,800,80,20,6,2.5,1.26,
                  1,0.79,0.40,0.16,0.072,0.0027,0.0004,0.00017])
                  
t = np.linspace(0,2*np.pi,100)\n",
u=3e4     #x-position of the center\n",
v=2e-3    #y-position of the center\n",
a=1000    #radius on the x-axis\n",
b=100   #radius on the y-axis\n",

fig , ax = plt.subplots()
ax.plot(T_star,L_star, marker = '*')
ax.plot(5777,1,marker='*',color='yellow', label='Sol')
#ax.plot(u+a*np.cos(t),v+b*np.sin(t), color = 'black')# Sol\n",
for i in range(len(R_list)):\n",
    ax.plot(Teff, L(Teff,R_list[i])/L_sun, '--' , color='grey')
    
# Supergigantes
#supergigantes = Ellipse(xy=(5*10**4,10**-3),width=100,height=0.0005)
#ax.add_patch(supergigantes)

# Text
ax.text(9*10**4,10**5,r'$R_{\odot}$')
ax.text(9*10**4,10**1,r'0.01$R_{\odot}$')
ax.text(9*10**4,10**-3,r'0.0001$R_{\odot}$')
ax.text(10**4,10**5,r'$100R_{\odot}$')
ax.text(2.5*10**3,10**5,r'10000$R_{\odot}$')
ax.text(4*10**3,2*10**-5,'Secuencia Principal',rotation = -45)

# Decoracion
ax.set_facecolor('#f7f7f7')
ax.set_xscale("log")
ax.set_yscale("log")
ax.spines['left'].set_color('#0a351c')
ax.spines['bottom'].set_color('#0a351c')
ax.spines['right'].set_color((.8,.8,.8))
ax.spines['top'].set_color((.8,.8,.8))
ax.tick_params(colors='#0a351c',which='both',direction='in')
ax.xaxis.label.set_color('#0a351c')
ax.yaxis.label.set_color('#0a351c')

ax.set_xlim(10**5,10**3)
ax.set_ylim(10**-6,10**6)
ax.set_ylabel(r'$\log (L/L_{\odot})$',fontsize=11)
ax.set_xlabel(r'$\log  T_{eff}$ [K]',fontsize=11)
ax.legend()
