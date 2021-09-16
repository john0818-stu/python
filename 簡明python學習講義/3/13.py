n = int( input("> ") )

for i in range (7) :
        
        for t in range(n) :
                
                for j in range (5) :
        
                        for s in range(n) :
                                if j == 2 or i == 2 or i == 4 or ( i == 3 and ( j == 0 or j == 4 ) ) :
                                        
                                        print( "a" , end="" )
                                        
                                else :

                                        print( " " , end="" )
                                        
                print()

