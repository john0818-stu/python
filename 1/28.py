n = int ( input ( "> ") )

for i in range (n) :
    
    print( " "*(n*(n-1)) + str(n)*(n) )
    
for m in range (n-2,-1,-1) :
    
    for i in range (n,0,-1) :
        
        print( " "*n*m + str(m+1)*n + " "*n*(2*n-3-2*m) + str(m+1)*n )

    
