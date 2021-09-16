import pylab 

from math import*

from numpy import *
    
x = linspace( -2*pi , 2*pi , 500 )

y = sin( x )

pylab.title( "sin(x)" ) #設定標題

pylab.ylabel( "sin(x)" ) #設定y軸標題

pylab.grid( ls = ":" )

pylab.fill_between( x , y , 0   , where = x > 5   , color="g" )

pylab.fill_between( x , y , -0.5   , color="r" )

pylab.fill_between( x , y , 0  , color="c" )
 
pylab.fill_between( x , y , 0.5  , color="b" )

pylab.plot()

pylab.show()
