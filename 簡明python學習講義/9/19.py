import pylab

from math import *

from numpy import *

from random import *

ans = {}

s = 7

ts = linspace( 0 , 2*pi , 5 ) + 45*pi/180

with open( "cbitmap.dat" , "r" , encoding="utf8" ) as infile :

    aa , bb = zip( *[ x.split( ' ' , 1 ) for x in infile ] )

for i , a in enumerate( aa ) :

    ans[a] = [ int( x , 16) for x in  bb[i].split() ]

def main() :

    n = [ x for x in input("> ") ]

    for i in range( s ) :

        for f , ch in enumerate(n) :

            for j in range( s-1 , -1 , -1 ) :

                if ( ans[ch][i] >> j )%2 :

                    xx = cos(ts)*sqrt(2) - j*2 + 16*f
                    
                    yy = sin(ts)*sqrt(2) - i*2 

                    cc = [ random() for i in range(3) ]
                        
                    pylab.fill( xx , yy , color = cc )

    pylab.axis( "off" )
                    
    pylab.show()

main()
