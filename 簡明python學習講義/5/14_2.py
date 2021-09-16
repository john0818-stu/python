import pylab

from math import *

from numpy import *

from random import *

g = ( 99 , 20 , 127 , 42 , 62 , 8 , 8 ) #倒過來 因為左下是( 0 , 0 )

ts = linspace(0,12*pi,1000)

for i in range (7) :

    for j in range (7) :

        x = [ sin( t )*( e**cos( t ) - 2*cos( 4*t ) - sin( t / 12 )**5 ) for t in ts]

        f = randrange( 0 , 200 , 25 ) / 100 #隨機選轉度數

        y = [ cos( t )*( e**cos( t ) - 2*cos( 4*t ) - sin( t / 12 )**5 ) for t in ts]

        a = array( [ [ cos( f*pi ) , -sin( f*pi ) ] , [ sin( f*pi ) , cos( f*pi ) ]  ] ) #選轉公式

        b = [ x , y ]

        c = dot( a , b ) + array( [ [ 8*i ] , [ 8*j ] ] )

        if ( g[ j ] & ( 1 << i ) ) :

            pylab.fill( c[0] , c[1] )
            
pylab.axis( "off" ) #顯示區域(前面加"off"關掉做標軸)

pylab.plot()

pylab.show()


