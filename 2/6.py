n = int ( input ( "> ") )

for i in range ( n ) :
    
    for j in range ( -( 2*n - 2  ) , 2*n - 1 ) :

        print( "*" if ( i == abs( j ) or i + abs( j ) == 2*n - 2 ) else " " , end="" )

    print()
        
