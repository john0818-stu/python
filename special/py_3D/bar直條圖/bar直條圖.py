infile = open("grades.txt" , encoding="utf-8" ) 

num , name , grade = list( zip( *[ x.split() for x in infile ] ) )

from numpy import *
import pylab
from mpl_toolkits.mplot3d import Axes3D

fig = pylab.figure( "grades_bar_3d" )
ax = Axes3D( fig )

x = [ i+1 for i , x in enumerate( grade ) ]
z = list( map( eval , grade ) )

ax.bar( x , z , zs = 0 , zdir="y" , color = "g" )
ax.bar( x , z , zs = 10 ,zdir="y" , color = "b" )
ax.bar( x , z , zs = 20 ,zdir="y" , color = "r" )

pylab.show()
