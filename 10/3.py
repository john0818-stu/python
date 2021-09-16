from random import shuffle 

col = "CDHS"

cards = []

for i in range( 52 ) :

    n = str( i%13 + 1 )

    if n in [ "1" , "11" ] :

        cards += [ col[ i//13 ] + ( "A" if n in "1" else "J" ) ]

    elif n in [ "12" , "13" ] :

        cards += [ col[ i//13 ] + ( "Q" if n in "12" else "K" ) ]

    else :
    
        cards += [ col[ i//13 ] + n ] 

shuffle( cards )

class Cards :

    def __rshift__( self , frac  ) :

        frac.all_card += [ cards[0] ]

        del cards[0]

        return frac
    
class Player( Cards ) :

    def __init__( self , n ) :

        self.all_card = []

        self.n = n

        self.all_card += [n] + [":"]

    def __str__( self ) :

        return " ".join( self.all_card )

if __name__ == "__main__" :
    
    a , b , c , d = Player( "Tom" ) , Player( "Sam" ) , Player( "Joe" ) , Player( "Amy" )

    deck = Cards()

    for i in range( 5 ) :

        deck >> a >> b >> c >> d

    print( a , b , c , d ,  sep = "\n")
