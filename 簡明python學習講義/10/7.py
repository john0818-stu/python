from random import *

class Dict :

    def __init__ ( self , name ) :

        self.n = name

        self.s = []

    def __str__( self ) :

        return "{} {} --> {}".format( self.n , " ".join( self.s ) , Dict.val( self ) )

    def name( self ) :

        return self.n

    def throw_dices( self ) :

        self.s = [ str( randint(1,6) ) for i in range(3) ]

    def val( self ) :
        
        if len( set( self.s ) ) == 3 :

            return 0

        else :

            n = list( map( int , self.s ) )
            
            return abs( 2*sum( list( set(n) ) ) - sum(n) )

if __name__ == "__main__" :
        
    a , b = Dict( "小明" ) , Dict( "小華" )

    while 1 :

        a.throw_dices()

        b.throw_dices()

        print( a , b , sep = "\n" , end="\n\n" )

        if a.val() != b.val() : break

    print( ( a.name() if a.val() > b.val() else b.name() ) + "贏" )
