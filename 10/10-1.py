class Poly :

    def __init__( self , *x ) :

        self.xx = list( x )

        for i in x :

            if type( i ) == list :
                
                self.xx = i

    def __str__( self ) :

        strx = [ self.gg( self.xx[0] ) ] + [ self.g( ch ) for i , ch in enumerate( self.xx[1:] )]

        ans = ""

        for i , ch in enumerate( strx ) :

            if ch != "0" :

                if i <= 1 :

                    ans += "{}x".format( ch  ) if i else ch

                else :

                    ans += "{}x^{}".format( ch , i )
                
        return ans[3:]
    
    @classmethod
    def vecform( cls , a , b ) :

        ss =  [ int(b) for i in range(a+1) ]

        return cls( ss )

    def __add__( self , foo ) :

        return Poly( self.f( foo , 1) )

    def __sub__( self , foo ) :

        return Poly( self.f( foo , -1) )

    def f( self , foo ,a ) :

        gi = min( len( self.xx ) , len( foo.xx ) )

        ga = max( len( self.xx ) , len( foo.xx ) ) 

        c = []

        for i in range( ga ) :

            if i < gi :

                c += [ self.xx[i] + a*foo.xx[i] ]

            else :

                c += [ a*foo.xx[i] if ga == len( foo.xx ) else self.xx[i] ]

        return c

    def g( self , x ) :

        if abs(x) == 1 :

            return " - " if x < 0 else " + "

        else :

            return ( " + " + str(x)+ " " ) if x > 0 else str(x)

    def gg( self , x ) :
        
        return ( " + " + str(x)  ) if x > 0 else str(x) 

if __name__ == "__main__" :

    a = Poly( 3 , 1 , 2 , -1 , -1 )

    print( a )

    b = Poly.vecform( 4 , 1 )

    print( b )

    c = a + b

    print( c )

    d = b - Poly.vecform( 2 , 1 )

    print( d )
