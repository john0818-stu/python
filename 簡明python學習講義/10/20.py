from random import *

def f( x ) :

    n = max( x )

    for i in range( 3*n+4 ) :

        for j in x :

            f = 2*j + 1 #房子的天花板

            h = j + 1 #房子身體

            w = 4*j + 1#房子寬度
                            
            d =  3*( n - j ) # 房頂 到 i = 0 距離
                    
            if i < d :

                print( " "*w , end=" " )

            elif i < d + f :

                g = d + f - i - 1

                if i == d :

                    print( " "*g + "*" + " "*g  , end=" " )

                else :

                    print( "{}/{}\{}".format( " "*g , "-"*( 2*i - 2*d - 1 ) , " "*g ) , end= " " )

            elif i < d + f + h :

                g = d + f + h - i - 1

                if g == 0 :

                    print( "|{}|".format( "="*( w - 2 ) ) , end=" "  )

                elif i == d + f and j <= 1   :

                    print( "|{}|".format( " "*( 4*j - 1 ) ) , end=" ")

                elif i == d + f :

                    print( "|{}{}{}|".format( " "*( j + 1 ) , "_"*( 2*j - 3 ) , " "*( j + 1 ) ) , end=" " )


                else :

                    print( "|{}|{}|{}|".format( " "*j , " "*( 2*j - 3 ) , " "*j ), end=" " )
                
            else :

                print( "II" + " "*(w-4) + "II" , end=" " )
                
        print( )
            

class Huts :

    def __init__( self , x ) :

        self.size = x

    @classmethod
    def from_array( cls , foo ) :

        return cls( foo )

    def show( self ) :

        return f( self.size )

    def sort( self , x ) :

        self.size = [ i for i in sorted( self.size , key = x ) ]

        return self

    def shuffle( self ) :

        shuffle( self.size )

        return self

    def __iadd__( self , i ) :

        self.size += [i]

        return self

    def __setitem__( self , i , x ) :

        self.size[i] = x

        return self
    
if __name__ == "__main__" :

    foo = [ 2 , 1 , 2, 1 , 2 ]

    huts = Huts.from_array( foo )

    huts.show()

    print( "> 由小到大排列: " )

    huts.sort( lambda x : x ).show()

    print( "> 隨意排列")

    huts.shuffle().show()

    print( "> 加一間 2 號房: ")

    huts += 2

    huts.show()

    print( "> 第一間變成 3 號房舍: ")

    huts[0] = 3

    huts.show()

    
