from numpy import *
import pylab
from mpl_toolkits.mplot3d import Axes3D

fig = pylab.figure( "john" , figsize = ( 8 , 8 ) )
ax = Axes3D(fig)

z = linspace(0, 1, 100)
x = z * sin(20 * z)
y = z * cos(20 * z)
col = x + y

#ax.plot3D(x, y, z, 'gray')
ax.scatter( x , y , z , c = col , marker = '+' )

pylab.show()
