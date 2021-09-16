n = int ( input ( "> ") )

for i in range (n):
    
    for t in range (n):
        
        print( " "*(n-i-1) + "/\\"*(i+1) + " "*(n-i-1) , end=" " )
        
    print()
