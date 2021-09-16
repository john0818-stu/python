n = int ( input ( "> ") )
                

for s in range (n):

        for i in range (n):
                
                print(" "*(n-1-s)*n,end="")
                
                for h in range (2):
                        
                        print(" "*2*(n*h*(n-s-2)),end="")

                        for t in range (s+1):     
                        
                                print(end=" ")
                        
                                for j in range (2*n-1) :
                                
                                        if ( -i+j==n-1 or i+j==n-1 or i==n-1 ) and ( h!=1 or s!=n-1 or t!=n-1 ) :
        
                                                print(i+1,end="")
                                        else :
                                        
                                                print(" ",end="")
                print()
                
for s in range (n-1,-1,-1):

        for i in range (n-1,-1,-1):

                if i!=n-1 or s!=n-1:
                        
                        print(" "*(n-1-s)*n,end="")
                
                        for h in range (2):
                        
                                print(" "*2*(n*h*(n-s-2)),end="")

                                for t in range (s+1):     
                        
                                        print(" ",end="")
                        
                                        for j in range (2*n-1) :
                                
                                                if ( -i+j==n-1 or i+j==n-1 or i==n-1 ) and ( h!=1 or s!=n-1 or t!=n-1 ) :
        
                                                        print(i+1,end="")
                                                else :
                                        
                                                        print(" ",end="")
                        print()
