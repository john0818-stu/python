n = int ( input ( "> " ) )

for j in range (n-1):
    
    print( 1 , end=" ")
    
print(2)

for j in range(n-2):
    
    print( 4 , " "*(2*n-3) , 2 , sep="")
    
print( "4" + " 3"*(n-1))
