from random import*

n = int( input( "> " ) )

a = [ i for i in range( n , n*6 + 1) ]

b = [ 0 for i in range( n , 6*n + 1 ) ]

t = 1000

for total in range( t ):

    s = 0

    foo = [ randint(1,6) for i in range( n ) ]

    for x in foo :

        s += x

    for k in range( 6*n - n + 1 ) :

        if s == a[ k ] :

            b[ k ] += 1
            

l=len(str(6**n))          

for i in range(n,6*n+1):

    print( "{:>{}}".format( i , l ),end=" " )

print()

for i in range(n,6*n+1):

    print( "="*l , end=" " )

print()

for i in range( 5*n + 1 ):

    print( "{:>{}}".format( b[ i ] , l ),end=" ")

print()

for i in range( 5*n + 1  ):

    print( '-'*l , end=" ")

print()

for i in range( 5*n + 1 ):

    print( "{:>}".format(6**n),end=" " )

print()



