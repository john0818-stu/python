import pylab

from math import *

from numpy import *

from random import *

n = int ( input( "> "))

ts = linspace(0,12*pi,1000)

for s in range ( n ) :

    i = 8*s

    x = [ i + sin( t )*( e**cos( t ) - 2*cos( 4*t ) - sin( t / 12 )**5 ) for t in ts]

    for s in range ( n ) :

        s = 6*s

        y = [ s + cos( t )*( e**cos( t ) - 2*cos( 4*t ) - sin( t / 12 )**5 ) for t in ts]

        pylab.fill( x , y , color=( random() , random() , random() ) )

pylab.axis( "off" ) #顯示區域(前面加"off"關掉做標軸)

pylab.show()

