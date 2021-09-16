import pylab
 
from numpy import *
 
from random import *
 
bmap=((15,9,9,9,15),(2,2,2,2,2),(15,1,15,8,15),(15,1,15,1,15),(9,9,15,1,1),(15,8,15,1,15),(15,8,15,9,15),(15,1,2,2,2),(15,9,15,9,15),(15,9,15,1,15))
 
ts = linspace( 45 , 360-45 , 4 )*pi/180
 
n = list( map( int , input("> ") ) )

c = [ [ random() for i in range(4) ] for i in n ]
 
for ii in range(5) :
 
    for i in range( 5 ) :
         
        for s , ch in enumerate(n) :
            
            for jj in range( 3 , -1 , -1 ) :

                for j in range( 3 , -1 , -1 ) :

                    if ( bmap[ ch ][ i ] >> j )%2 and ( bmap[ ch ][ ii ] >> jj )%2  :
 
                        x = cos(ts)*sqrt(2) - 2*j + 5*11*s - 11*jj
 
                        y = sin(ts)*sqrt(2) - 2*i - 11*ii
                         
                        pylab.plot( x , y , color = c[s] , lw=5 )

pylab.axis("off")

pylab.show()
               
