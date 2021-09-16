n = int( input("> ") )

for s in range(n):
        
        for i in range(3):
                
                for t in range(n):
                        
                        for j in range(3):
                                
                                if  s == t or s + t == n-1 :
                                            
                                        print( n , end="" )
					    
                                else :
                                            
                                        print( " " , end="" )
					    
                print()
