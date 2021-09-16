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

            ans += "X^{}".format( i ) if i > 1 else ""

            ans += "X" if i == 1 else ""

    return ans
        
class Poly :

    def __init__( self , *x ) :

        self.xx = list( x ) if type( x[0] ) != list else list( x[0] )
        
    def __str__( self ) :

        return new_str( f( self.xx ) )

    def derivative( self ) :

        s = [ ch*i for i , ch in enumerate( self.xx ) ][1:]
        
        return Poly( s )
    
    def val( self , x ) :

        ans = ""

        for i , ch in enumerate( self.xx ) :

            ans += "+" + str(ch) + "*x**{}".format(i)

        return float( eval( ans ) )

    def integral( self ) :

        s = [ ch//( i + 1 ) for i , ch in enumerate( self.xx )  ]

        return Poly( [0] + s )

    def integral_over( self , a , b ) :

        return self.integral().val( b ) - self.integral().val( a )
        
if __name__ == "__main__" :

    a = Poly( 5 , -2 , 3 , -12 )

    print( "多項式 :" , a )

    print( "微分函數 :" , a.derivative() )

    print( "微分函數在 x = 1 值 :" , a.derivative().val(1) )

    print( "積分函數 :" , a.integral() )

    print( "積分函數 x = 2 值 :" , a.integral().val(2) )

    print( "在 [ 0 , 1 ] 的定積分 :" , a.integral_over( 0 , 1 ) )

