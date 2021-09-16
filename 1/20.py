n = int ( input ( "> ") )

print( str( 1 ) * ( 2*n-1 ) )

for i in range (n-2) :
    
    print( 1 , " "*(2*n-3) , 1 , sep="")
    
print( str( 1 ) * ( 2*n-1 ) )

for s in range(1,3):
    
    for t in range(s+1):   
        
        for j in range(2*n-1):
            
            print( 2*s+t , end="" , sep="" )

        print( end="D" )
            
    print()
    
    for i in range(n-2):

        for t in range(s+1):
            
            print( 2*s+t , " "*(2*n-3) , 2*s+t , end=" " , sep="" )
               
        print()
        
    for t in range(s+1):

        for j in range(2*n-1):
            
            print( 2*s+t , end="" )

        print( end=" " )
            
    print()
