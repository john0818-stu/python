
from random import *

def main() :

    m , s , n = (randint(2,4) for i in range(3))

    a = set_matrix( m , s , 2 )
        
    b = set_matrix( s , n , 2 )

    t = [ a , b ]

    for i in range(2) :

        print( "{} :".format( chr( ord("A") + i ) ) )

        for d in t[i]  :

            print( "  ".join( map( str , d ) ) )

    print( "C :" )

    for x in a :

        for y in zip( *b ) :

            print( sum([ h[0]*h[1] for h in zip(x,y) ]) , end="  " )

        print()

def set_matrix( m , s , i ) :

    a = [ [ randint(0,2) for i in range(s) ] for j in range(m) ]
    return a 

main()
