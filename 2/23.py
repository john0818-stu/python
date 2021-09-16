n = int ( input ( "> ") )

for i in range ( n-1 , -n , -1 ) :
            
    for j in range ( 3*n - 3  , -( 3*n - 2 ) , -1 ) :

            
            if abs( j ) == abs( i ) or abs(j) + abs(i) == 2*n-2 or abs(j) - abs(i) ==  2*n-2 or abs(i) + abs(j) == n-1 :

                print( "*" , end=" " )

            else :

                print( " " , end=" " )
 
    print()                    
    
