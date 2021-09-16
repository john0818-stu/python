from numpy import *
import pylab 
from matplotlib import animation 

fig = pylab.figure()

x = linspace( 0 , 2*pi , 100 )
y = sin(x)

pylab.plot( x , y )
point_ani, = pylab.plot( x[0] , x[0] )
pylab.grid(ls="--")

def update_points( num ) :
    if num%5==0:
        point_ani.set_marker("*")
        point_ani.set_markersize(12)
    else:
        point_ani.set_marker("o")
        point_ani.set_markersize(8)
        point_ani.set_data(x[num], y[num])
        #text_pt.set_text("x=%.3f, y=%.3f"%(x[num], y[num]))
    return point_ani,


ani = animation.FuncAnimation(fig, update_points, arange(0, 100), interval=100, blit=True)


pylab.show()
