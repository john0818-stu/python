n = int ( input ( "> ") )

for i in range ( -n+1 , n ) :
    
    for j in range ( -n+1 , n ) :

        s , t = abs(i) , abs(j)
        
        print( abs( n - max( s , t ) ) ,end=" " )
        
    print()
            
