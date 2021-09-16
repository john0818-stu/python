n = int ( input ( "> ") )

for t in range (n):
    
    print( " "*(n-1) + str(1) + " "*(n-1) , end=" " )
    
print()

for i in range (1,n-1):
    
    for t in range (n):
        
        print( " "*(n-i-1) + str(i+1) + " "*(i+i-1) + str(i+1) + " "*(n-i-1) , end=" ")
        
    print()
    
for i in range (n-1,n):
    
    for t in range (n):
        
        print( " "*(n-i-1) + str(i+1)*(2*i+1) + " "*(n-i-1) , end=" " )
        
    print()
