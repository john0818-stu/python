import pylab

from numpy import *

from random import *

ts = linspace( 0 , 10*pi , 1000 )

gg = ( 8 , 8 , 127 , 73 , 127 , 8 , 8 )  , ( 99 , 20 , 127 , 42 , 62 , 8 , 8 )

fs = lambda t : sin( t )*( e**cos( t ) - 2*cos( 4*t ) - sin( t / 12 )**5 )
fc = lambda t : cos( t )*( e**cos( t ) - 2*cos( 4*t ) - sin( t / 12 )**5 )


for k , g in enumerate( gg )  :
    
    for i in range (7) :

        for j in range (7) :

            x = [ fs(t) for t in ts]

            y = [ fc(t) for t in ts]

            f = randrange( 0 , 200 , 25 ) / 100 #隨機選轉度數

            a = array( [ [ cos( f*pi ) , -sin( f*pi ) ] , [ sin( f*pi ) , cos( f*pi ) ]  ] ) #選轉公式

            c = dot( a , [ x , y ] ) + array( [ [ 8*i + k*70 ] , [ 8*j ] ] )

            if ( g[ j ] & ( 1 << i ) ) :

                pylab.fill( c[0] , c[1] )

pylab.axis("off") #顯示區域(前面加"off"關掉做標軸)

pylab.show()



