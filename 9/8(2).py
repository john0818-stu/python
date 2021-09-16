from random import *

def main() :

    global number 

    n = input("> ")
    
    a = len(n)

    num = [  str(0) + str(i) for i in range(10**(a-2) , 10**(a-1)) if len( set( str(0) + str(i)) ) == a ]

    ber = [  str(i) for i in range( 10**(a-1) , 10**a ) if len( set( str(i)) ) == a ]

    number = num + ber

    a = choice( number )

    print( 1 , a , end=" ")

    print( "{}A {} B".format( *f(n,a) ) )

    print()

    df( a , n )

    dd = 2
        
    while 1 :

        if f(a,n) == [len(n),0] :

            break
        
        a = choice( s( a , f(n,a) ) )

        print(dd , a , end=" ")

        print( "{}A {} B".format( *f(n,a) ) )

        print( len( number ) )

        print()

        dd += 1
        df( a , n )

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

def s( a , n ) :

    ans = {}

    for i in range(5) :

        for j in range(5) :

            ans[ str( [i,j] ) ] = 0
            
    for i in number :
    
        ans[ str( f( a , i ) ) ] += 1

    for s in ans :

        if ans[s] == max( ans.values() ) :

            break

    print( s )
        
    t = set()
    
    for i in number :

        for j in number :

            if str( f( i , j ) ) == s :

                t.add(i)
                t.add(j)

    print( len( list(t) ) )
                
    return list(t)   
                
            
main()

    
        
    

