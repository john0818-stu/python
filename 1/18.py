n = int ( input ( "> ") )

for i in range (n-1,-1,-1):
    
    print( " "*(n+1)*(n-i-1) , end="" )
    
    for t in range (i,-1,-1):
        
        for j in range (n):
            
            print( t+1 , end="" )

        print( end=" " )
            
    print()
