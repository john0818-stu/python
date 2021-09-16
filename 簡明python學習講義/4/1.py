n = int( input("> ") )

a = 2*n - 1

nums=[ [ 0 ]*a for i in range( a ) ]

for i in range (a) :

    for j in range(a) :

        if j + i <= a - 1 :
            
            nums[i][j] = abs( n - min( i , j ) )

        else :

            nums[i][j] = abs( max( i , j ) - n + 2 )

        
            

       
for i in range ( a ):
    
    for j in range ( a ):
        
        if ( i >= j >= n - 1 ) or  ( i <= j <= n - 1 ) or ( n + j <= i + j + 1 <= a ) or ( n + j >= i + j + 1 >= a ) :

            print( "{}".format( nums[ i ][ j ] ) , end=" " )

        else :

            print( " " , end=" " )
            
    print()
    


        
        
