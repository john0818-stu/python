import pylab

from math import *

from numpy import *

from random import *

n = int ( input( "> "))

ts = linspace( 0 , 12*pi , 1000 )

for i in range ( n ) :

    s = 8*i

    x = [ s + sin( t )*( e**cos( t ) - 2*cos( 4*t ) - sin( t / 12 )**5 ) for t in ts]

    for j in range ( n ) :

        a = 6*j

        y = [ a + cos( t )*( e**cos( t ) - 2*cos( 4*t ) - sin( t / 12 )**5 ) for t in ts]

        if i == j or  j + i == n - 1 :

            pylab.fill( x , y , color=( random() , random() , random() ) )

pylab.axis( "off" ) #顯示區域(前面加"off"關掉做標軸)

pylab.show()

