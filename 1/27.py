n = int ( input ( "> ") )

for m in range (n-1) :

    for i in range (n) :
        
        print( " "*n*m + str(m+1)*n + " "*n*(2*n-3-2*m) + str(m+1)*n )
        
for i in range (n) :
    
    print( " "*(n*(n-1)) + str(n)*(n) )
    
    
        



