n = int ( input ( "> ") )

for i in range ( n+n-1 ) :
    
    for t in range (n) :
        
        for j in range ( n ) :
                
            print( ( t+1 if 0 + t <= i < n + t and ( j == 0 or j == n - 1 or i == n - 1 + t ) else " " ) , end="" )

        print( " " , end="" )
                
    print()
