n = int ( input ( "> ") )

for i in range ( n-1 , -n , -1 ):

    for j in range ( 2*n - 2 , -n , -1 ):
    
        if j - i == n - 1 or i == j <= 0 or  i + j == n - 1 or i +  j == -n + 1 or abs(i) + abs(j) == n - 1 or -i == j < 0  :
            
             print( "x" , end=" " )

        else :
                    
                                   
            print( " " , end=" " )

    print()
