from numpy import *

def f( x ) :

    s = []

    for i , ch in enumerate( x ) :

        if i == 0 :

            s += [ str( ch ) ]

        elif abs( ch ) != 1 :

            s += [ " - " + str( abs( ch ) ) ] if ch < 0 else [ str( ch ) ]

        else :

            s += [ " - " ] if ch < 0 else [ "" ]

    return s

def new_str( x ) :

    ans = ""

    f = 0

    for i , ch in enumerate( x ) :

        if ch != "0" :

            ans += " + " if "-" not in ch and i and f else ""

            f += 1 

            ans += ch

            ans += " " if len( ch ) and i and ch[-1] not in " " else ""

            ans += "x^{}".format( i ) if i > 1 else ""

            ans += "x" if i == 1 else ""

    return ans

def g( a , b ) :

    s = max( len(a) , len(b) )

    r = []

    for i in range( s ) :

        if i < len(a) :

            r += [ str( a[i] ) ]

        else :

            r += [ '0' ]
            
    return list( map( int , r ) ) 
        
class Poly :

    def __init__( self , *x ) :

        self.xx = list( x ) if type( x[0] ) != list else list( x[0] )

    def __str__( self ) :

        return new_str( f( self.xx ) )

    @classmethod
    def vecform( cls , a , b ) :

        xx = [ int( b ) for i in range( a + 1 ) ]
        
        return cls( xx )
    
    def __add__( self , foo ) :

        s = array( g( foo.xx , self.xx ) ) + array( g( self.xx , foo.xx ) )
    
        return Poly( list( s ) )

    def __sub__( self , foo ) :

        s = array( g( self.xx , foo.xx ) ) - array( g( foo.xx , self.xx ) )

        return Poly( list( s ) )
        
if __name__ == "__main__" :

    a = Poly( 3 , 1 , 2 , -1 , -1 )

    print( a )

    b = Poly.vecform( 4 , 1 )

    print( b )

    c = a + b

    print( c )

    d = b - Poly.vecform( 2 , 1 )

    print( d )

