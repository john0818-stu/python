n = int ( input ( "> ") )

for s in range(3):
    
    for i in range(n):
        
        for t in range(3):
            
            for j in range(n):

                if  ( s == t or s + t == 2 ) and ( i == j == n//2  ):

                    print( "x" , end="" )

                elif   ( s == t or s + t == 2 ) and ( i ==j or i + j == n -1 )  :                            

                    print( "\\" if i ==j else "/" , end="" )
                                
                else :

                    print( " "  , end="" )
                        
        print()
