import pylab

from numpy import *

from random import *

ans = {}

with open ( "cbitmap.dat" , "r" , encoding="utf8" ) as infile :

        for ch in infile :

            a , *x = ch.split()

            ans[a] = [ int( i , 16 ) for i in x ]
            
ts = linspace( 0 , 2*pi , 1000 )

tx = sin( ts )*( e**cos( ts ) - 2*cos( 4*ts ) - sin( ts / 12 )**5 )

ty = cos( ts )*( e**cos( ts ) - 2*cos( 4*ts ) - sin( ts / 12 )**5 )

ss = 7

while 1 :

    n = input("中央一百> ")

    for i in range( ss ) :

        for j , ch in enumerate(n) :

            for s in range( ss-1 , -1 , -1 ) :

                if ( ans[ch][i] >> s )%2 :

                    rt = randint(0,364)*pi/180

                    rs , rc = sin(rt) , cos(rt)

                    x = tx*rs - ty*rc - s*8 + 10*j*ss

                    y = tx*rc + ty*rs - i*8

                    pylab.fill( x , y  )
                
    pylab.axis("off") #顯示區域(前面加"off"關掉做標軸)

    pylab.show()

