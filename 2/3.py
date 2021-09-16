h , n = eval( input( ">　" ) )

a = len( str( h ) ) # h 長度

b = len( str( n ) ) # n 長度

c = len( str( h*n ) ) # h*n 長度

print( " "*( c - a + 1  ) , h , sep="" )

print( "x"," "*( c - b ) , n , sep="" )

print( "-"*( c + 1 ) )

for i in range ( 1 , b+1 ):
    
    s = ( n % ( 10 ** i ) - n % ( 10 ** (i-1) ) ) // ( 10**(i-1) )

    s1 =len( str( s*h ) )

    if s == 0 :

        continue 
    
    print(" "*( c - s1 - i + 2 ) , s*h , sep="" )
    
print( "-"*( c + 1 ) )

print(" " , n*h , sep="" )


    
