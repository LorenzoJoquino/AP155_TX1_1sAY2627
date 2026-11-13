import numpy as np
import matplotlib.pyplot as plt
from Bessel import J

#I = ((J1*k*r)/(k*r))**2

def density_plot(r,wavelength=500e-9): #r is max value given r min =0
    #r into 2 dimensions
    x=np.linspace(-r,r,1001)
    y=np.linspace(-r,r,1001)
    X,Y = np.meshgrid(x,y)
    R = np.sqrt(X**2+Y**2)
    k=2*np.pi/wavelength
    kR=k*R
    #vectorizing j1
    j1_vec = np.vectorize(lambda val: J(1,val)) #slow since it integrates 1000 points, optimize later
    j1_grid = j1_vec(kR)

    #calculating I
    I=(j1_grid/kR)**2
    #plotting using imshow
    plt.title(r'Diffraction pattern of a light source with $\lambda = 500 nm$')
    plt.xlabel('x')
    plt.ylabel(r'$I(r)$')
    plt.imshow(I, cmap='hot', vmax=0.01)
    return plt.show()
    