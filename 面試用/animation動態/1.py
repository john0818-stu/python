from numpy import *
import pylab
from matplotlib import animation

fig1 = pylab.figure()

x = linspace( 0 , 2*pi , 100 )
plot_sin, = pylab.plot( x , sin(x) )
h = 0
def update(i) :
    
    a = x + h
    h += 1 
    plot_sin.set_ydata( sin(a) )
    return plot_sin,

def init() :
    plot_sin.set_ydata( sin(x) )
    return plot_sin,

while (1) :

    ani = animation.FuncAnimation( fig = fig1 , func = update , frames=1000 , init_func=init , interval=20 , blit = True )
    pylab.show() 
