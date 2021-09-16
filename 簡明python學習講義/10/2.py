from random import shuffle 

class Random_Shuffle :

    def __init__( self , n , d ) :

        self.n , self.d  = n , d       

    def len( self ) : return 1 #不知道要幹嘛

    def get( self ) :

        if type( self.n ) == int :

            ans = [ str(i) for i in range( self.n , self.d + 1 ) ]

        else :

            ans = [ chr(i) for i in range( ord( self.n ) , ord( self.d ) + 1 ) ]

        shuffle( ans )
        
        return " ".join( ans )

if __name__ == "__main__" :
    
    foo = Random_Shuffle( 8 , 11 )

    for i in range( 4*foo.len() ) :

        print( foo.get() , end=" " )

    print()
        
    bar = Random_Shuffle( "a" , "e" )

    for i in range( 2*bar.len() ) :

        print( bar.get() , end=" " )

    print()
