n = int ( input ( "> ") )

k=4

print( 1 , "-"*( 4*n-5 ) , 2 , "-"*( 4*n-5 ) , 3 , sep="" )

for i in range (1,n-1) :
    
    print("  "*(i),k%10,'-'*( 4*n-5-4*i ) , (k+1)%10 ," "*( 3+4*(i-1) ), (k+2)%10 ,'-'*( 4*n-5-4*i ) , (k+3)%10 , sep="")
    
    k=k+4
    
print( "  "*(i+1) , k%10 , " "*(2*(2*(n-2))+3) , (k+1)%10 ,sep="" )
