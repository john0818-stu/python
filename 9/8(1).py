from random import *

def main() :

    global number 

    n = input("> ")
    
    a = len(n)

    num = [  str(0) + str(i) for i in range(10**(a-2) , 10**(a-1)) if len( set( str(0) + str(i)) ) == a ]

    ber = [  str(i) for i in range( 10**(a-1) , 10**a ) if len( set( str(i)) ) == a ]

    number = num + ber

    dd = 1

   

    while 1 :

        a = choice( number )

        if f(n,a) == [0,0] : break

    print( dd , a , end=" ")

    print( "{}A {} B".format( *f(n,a) ) )

        

    print()

    dd += 1
    df( a , n )

    print( len(number) )
        
    while 1 :
        
        a = choice( number )
        

        print( dd , a , end=" ")

        print( "{}A {} B".format( *f(n,a) ) )

        

        print()

        dd += 1
        df( a , n )

        print( len(number) )

        if f(a,n) == [len(n),0] :

            break

def df( n0 , n ) :

    
    
    for i , x in enumerate( number ) :

        if f( n0 , n ) != f( x , n0 ) :

            del number[i]
            
def f( x , n ) : 

    a , b = 0 , 0
    
    for i , ch in enumerate( x ) :

        if n[i] == ch :

            a += 1

        elif ch in n :

            b += 1

    return [ a , b ]


                
            
main()

    
        
    

