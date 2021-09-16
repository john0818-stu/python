n = int ( input ( "> ") )

for s in range (n) :
        
        for i in range (n) :
                
                print( "+"*(n-1-s)*n , end="")
                
                for h in range (2) :
                        
                        print( "a"*2*(n*h*(n-s-2)) , end="")
                        
                        for t in range (s+1) :
                                
                                if h!=1 or s!=n-1 or t!=n-1:
                                        
                                        print( " "*(n-1-i) + str(i+1)*(2*i+1) + " "*(n-1-i) , end=" ")
                                        
                print()


	


                
        

