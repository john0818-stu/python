n = int ( input ( "> ") )

for s in range (n) :
        
        for i in range (n) :
                
                print( ""*(n-1-s)*n , end="")
                
                for t in range (s+1) :
                        
                        for j in range (2*n-1) :
                                
                                print( ( t+1 if -i+j==n-1 or i+j==n-1 or i==n-1 else " " ) , end="" )

                        print( end=" " )
                                
                print()
