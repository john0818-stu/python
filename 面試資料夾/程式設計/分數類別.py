def gcd( a, b ) :

    a , b = abs(a) , abs(b)

    if a > b :

        return gcd( a%b , b )  if a%b else b 

    else :

        return gcd( b%a , a ) if b%a else a
    
class Fraction : 

    def __init__( self , n , d = 1 ) :

        n , d = str(n) , str(d)

        if n.isdigit() :

            self.n , self.d = map( int , [ n , d ] )

        else :

            self.n , self.d = map( int , n.split("/") )

    def __str__( self ) :

        a = self.n//gcd( self.n , self.d )

        b = self.d//gcd( self.n , self.d )

        if b == 1 :

            return str(a)

        else :
            
            return str( a ) + "/" + str( b )
    
    def __add__( self , frac ) :

        n = self.n*frac.d + self.d*frac.n

        d = self.d*frac.d

        return Fraction( n , d )

    def __sub__( self , frac ) :

        n = self.n*frac.d - self.d*frac.n

        d = self.d*frac.d

        return Fraction( n , d )

    def __mul__( self , frac ) :

        n = self.n*frac.n

        d = self.d*frac.d

        return Fraction( n , d )

    def __truediv__( self , frac ) :

        n = self.n*frac.d

        d = self.d*frac.n

        return Fraction( n , d )

    #<
    def __lt__( self , frac ) :

        return True if self.n*frac.d < frac.n*self.d else False

    #==
    def __eq__( self , frac ) :

        return True if self.n*frac.d == frac.n*self.d else False

    #>=
    def __ge__( self , frac ) :

        return not( self < frac )

    #!=
    def __ne__( self , frac ) :

        return not( self == frac )

    #<=
    def __le__( self , frac ) :

        return ( self == frac or self < frac )

    #>
    def __gt__( self , frac ) :

        return not( self <= frac )

    @classmethod
    def date_doc( cls ) :

        return "n : 分子 , d : 分母"
