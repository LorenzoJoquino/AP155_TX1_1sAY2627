import numpy as np

def integrand(m,x,theta): #integrand inside J_m(x)
    return np.cos(m*theta -x*np.sin(theta))
	
def J(m,x,n=1001):
    theta = np.linspace(0,np.pi,n) #grid with end points 0 and pi
    a=0; b=np.pi #end points
    h = (b-a)/(n-1) #grid spacing, n-1=1000
    cs= 2*np.ones(n)
    cs[1::2] =4; cs[0] = 1; cs[-1]=1 #weighs
    contribs = cs*integrand(m,x,theta)
    return 1/np.pi*(h/3)*np.sum(contribs)