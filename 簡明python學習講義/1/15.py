n = int ( input ( "> ") )

for s in range(n):
    
    for i in range(n):
        
        print( str(2*i+1)*(n-s) + "/" + str(2*i+2)*(s+1),end=" ")
        
    print()
	
