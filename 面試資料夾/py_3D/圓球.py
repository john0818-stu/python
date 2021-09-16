from numpy import *
import pylab
from mpl_toolkits.mplot3d import Axes3D

fig = pylab.figure( "john" , figsize = ( 8 , 8 ) )
ax = Axes3D(fig)

u = linspace( 0 , 2*pi , 100 )
v = linspace( 0 , pi , 100 )

x = outer( cos(u) , sin(v) )
y = outer( sin(u) , sin(v) )
z = outer( ones(size(u)) , cos(v) )

ax.plot_surface(x, y, z)

pylab.show()
