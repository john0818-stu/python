import pylab 

from math import*

from numpy import *

from random import *

h = 1e-6

f = lambda x : cos( x )

df = lambda x :  ( f( x + h ) - f( x ) )/h

ddf = lambda x : "x"+str(x)
    
x = linspace( 0 , 1.5*pi , 100 )

y = cos( x )

pylab.title( "Newton method" ) #設定標題

pylab.ylabel( "cos(x)" ) #設定y軸標題

pylab.grid( ls = "--" )

x0 = 0.43

for i in range (1 , 6 ) :

    a = ( random() , random() , random() )

    pylab.arrow( x0 , f( x0 ) , 0 , -f( x0 ) , color = a , ls = "--")

    pylab.text( x0 - 0.1 , -0.1 , ddf( i - 1 ) ) 

    x1 = x0 - f( x0 ) / df( x0 )

    pylab.arrow( x0 , f( x0 ) , x1 - x0 , -f( x0 ) , color = a , ls = "--")

    x0 = x1

pylab.plot( x , y  )
 
pylab.show()
