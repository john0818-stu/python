bmap=((15,9,9,9,15),(2,2,2,2,2),(15,1,15,8,15),(15,1,15,1,15),(9,9,15,1,1),(15,8,15,1,15),(15,8,15,9,15),(15,1,2,2,2),(15,9,15,9,15),(15,9,15,1,15))

def f( x ) :

    for i in range( 5 ) :

        for n , ch in enumerate( x ) :

            for t in range( 3 , -1 , -1 ) :

                print( ch if ( bmap[ int(ch) ][i]>>t )%2 else " "  , end="" )

            print( end=" " )

        print()
    
class Bitmap :

    def __init__( self , n ) :

        self.n = [ i for i in str( n ) ]

    def __str__( self ) :

        f( self.n ) 
                    
        return ""
    
    def __iadd__( self , foo ) :

        ss = foo + int( "".join( self.n ) )
        
        return Bitmap( ss )

    def __ilshift__( self , foo ) :
    
        ss = "".join( self.n[foo:] + self.n[:foo] )

        return Bitmap( str( ss ) )

    def __irshift__( self , foo ) :
    
        ss = "".join( self.n[-foo:] + self.n[:-foo] )

        return Bitmap( str( ss ) )
        
if __name__ == "__main__" :

    num = Bitmap( 723456000 )

    print( num )

    num += 999

    print( num )

    num <<= 3

    print( num )

    num >>= 1
    
    print( num )
