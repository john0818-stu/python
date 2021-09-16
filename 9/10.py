import pylab

from numpy import *

def main () :

    x = linspace( -2*pi , 2*pi , 100 )

    y , z = sin(x) , sin(x)**3

    pylab.title( "Area between sin(x) and sin(x)**3 " )

    pylab.xlabel("x")

    pylab.ylabel("y")

    pylab.yticks( arange( 1 , -1.1 , -0.5 ) )

    pylab.grid( ls="--" )
    
    pylab.fill_between( x , y , z , color = "b" )

    pylab.show()
            
main()
 

    
        
    
