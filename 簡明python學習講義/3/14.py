n = int( input("> ") )

for m in range(5):
        
        for i in range(5):
                
                for s in range(n):
                        
                        for j in range(n):
                                
                                if m%2 == 0 or ( m == 1 and  s == n-1 ) or ( m == 3 and s == 0 ) :
                                        
                                        if i%2 == 0 or (i==1 and j==n-1) or (i==3 and j==0):
                                                
                                                print( "2" , end="" )
                                                
                                        else :
                                                
                                                print( " " , end="" )
                                                
                                else:
                                        
                                        print( " " , end="" )

                        print( " " , end="" )
                        
                print()
