n1 = int( input("> ") )

n = 4*n1 - 3



for a in range( 2*(n1) - 1 ):
        
        for t in range(2):
                                      
                for j in range(n) :

                        b = 2*n1 - 2 #最中間那行

                        if a == n1 - 1 :

                                print(  "/|\\" if t else "\|/" , end=" " )

                        elif ( j - a > 0 and a + j < b ) or ( j - a < 0 and a + j > b ) or ( j - a > b and a + j < 2*b ) or ( j - a < b and a + j > 2*b ) :

                                print( " "*3 , end=" " )
                                
                        else :
                                
                                print(  "/|\\" if t else "\|/" , end=" " )

                print()
