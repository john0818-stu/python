n = int ( input ( "> ") )

for i in range ( -n+1 , n ) :
    
    for j in range ( -n+1 , n ) :

        if -n < j + i < n and -n < j - i < n :
    
            print( abs( n - max( abs(i) , abs(j) ) ) , end=" " )

        else :

            print( " " , end=" ")
        
    print()

#print( abs( n - max( abs(i) , abs(j) ) ) if -n < j + i < n and -n < j - i < n else " "  , end=" " )
