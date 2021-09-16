from random import *

n = [ "剪刀" , "石頭" , "布  " ]

class SSP :

    def __init__ ( self , *name ) :

        self.n = [ i for i in name[0] ]

        self.p = []

    def __str__( self ) :

        if set( self.p ) == set( [n[0] , n[-1]] )  :

            self.ddel( n[-1] )
         
            return "---> " + n[0] + "\n"

        elif set( self.p ) == set( n[0:2] ) :

            self.ddel( n[0] )

            return "---> " + n[1] + "\n"

        elif set( self.p ) == set( n[1:3] ) :

            self.ddel( n[1] )

            return "---> " + n[2] + "\n"

        else :

            return "沒勝負" + "\n"

    def play( self ) :

        self.p = [ n[randint(0,2)] for i in self.n ]

        print( "{}\n{}".format( " ".join(self.n) , " ".join( self.p ) ) )

    def over( self ) :

        return 1 if len( self.n ) == 1 else 0

    def winner( self ) :

        return "".join( self.n )

    def ddel( self , f ) :

        d = [ i for i in self.n ]

        for i , ch in enumerate( self.n ) :
            
            if self.p[i] == f :

                d.remove( ch )

        self.n = d

if __name__ == "__main__" :

    players = ( "小草" , "小明" , "小民" , "花生" , "阿杰" )

    game = SSP( players )

    while 1 :

        game.play()

        print( game )

        if game.over() : break

    print( game.winner() )
