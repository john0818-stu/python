n = int ( input ( "> ") )

for s in range (n) :
    
    for i in range (n) :
                
        print( " "*(n-1-s)*n , end="")
                
        for t in range (s+1) :
                        
                print( end=" " )
                        
                for j in range (2*n-1) :
                                
                    if ( t==0 or t==s ) and (-i+j==n-1 or i+j==n-1 or i==n-1 ) :
        
                        print( i+1 , end="" )
                    
                    else :
                                        
                        print( " " , end="" )
                        
        print()

for s in range (n-1,-1,-1):
    
    for i in range (n-1,-1,-1):
                
        print(" "*(n-1-s)*n , end="" )
        
        if i!=n-1 or s!=n-1:
                    
            for t in range (s+1):     
                        
                print( end=" " )
                
                for j in range (2*n-1) :
                        
                    if ( t==0 or t==s ) and (-i+j==n-1 or i+j==n-1 or i==n-1 )  :
        
                        print( i+1 , end="")
                    else :
                                    
                        print( " " , end="")
                        
            print()
