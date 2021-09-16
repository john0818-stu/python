import pylab

from numpy import *

from random import *

def main() :

    while 1 :

        n = int( input("> "))

        f(n)

def f(n) :

    for i in range(n) :

        s = 360 / n
       
        sts = array( [  ( 90 - i*s )*pi/180 ,  ( 90 - (i+1)*s )*pi/180 , 0 ] )

        cts = array( [  ( 90 - i*s )*pi/180 ,  ( 90 - (i+1)*s )*pi/180 , pi/2 ] )

        x , y = sin(sts) , cos(cts)

        c = [ random() for i in range(4) ]

        pylab.fill( y , x , color = c )

    pylab.show()   
 
main()
