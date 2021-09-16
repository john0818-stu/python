n = int ( input ( "> ") )

for i in range(n):

        print( str( i+1 ) * ( i+1 ) + " "*( 2 * ( n-i-1 ) ) + str( i+1 ) * ( i+1 ) )
