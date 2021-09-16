n = int ( input ( "> " ) )

k = n + 1 

for j in range(n):
    
    print( (j+1)%10 , end=" " )
    
print()

for j in range( 1 , n-1 ):
    
    print(  k%10 , " "*(2*n-3) , (k + 1)%10 , end="\n" , sep="" )

    k = k + 2

for j in range(n):
    
    print( k%10 , end=" ")

    k = k + 1
