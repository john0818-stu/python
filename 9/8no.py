
from random import *

def main() :

    global n , number

    n = str( input("> ") ).strip()
    
    a = len(n)

    print( n )

    

    num = [  str(0) + str(i) for i in range(10**(a-2) , 10**(a-1)) if len( set( str(0) + str(i)) ) == a ]

    ber = [  str(i) for i in range( 10**(a-1) , 10**a ) if len( set( str(i)) ) == a ]

    number = num + ber

    shuffle(number)

    print("-------")

    n0 , n1 = number[0] , number[1]

    print( n0 , ":" , f( n0 , n ) )

    print( n1 , ":" , f( n1 , n ) )

    df( n0 , n )

    df( n1 , n )

    print()
    
    while 1 :

        print( len(number) )

        a = choice(number)

        print( a , ":" , f( a , n ) )

        print()

        df( a , n )
        
        if f( a , n ) == f( n , n ) :

            break

def df( n0 , n ) :

    for i , x in enumerate( number ) :

        if f( n0 , n ) != f( x , n0 ) :

            del number[i]

def f( x , n ) : 

    ans = { "A" : 0 , "B" : 0 }

    for i , ch in enumerate(n) :

        if ch == x[i] :

            ans["A"] += 1

        elif ch in x :

            ans["B"] += 1

    return " ".join( [ str(ans["A"]) , "A" , str(ans["B"]) , "B" ] )
            
main()

    
        
    

