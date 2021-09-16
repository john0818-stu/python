n = int ( input ( "> ") )

k = 1 

for i in range ( n-1 ) :
    
    print( " "*(2*i) , k%10 , "-"*( 4*n-5-4*i )  , (k+1)%10 , end="" , sep="")
    
    k=k+2
    
    print()
    
print( " "*(2*n-2) , k%10 , end="" , sep="" )
