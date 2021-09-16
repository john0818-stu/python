bmap=((15,9,9,9,15),(2,2,2,2,2),(15,1,15,8,15),(15,1,15,1,15),(9,9,15,1,1),(15,8,15,1,15),(15,8,15,9,15),(15,1,2,2,2),(15,9,15,9,15),(15,9,15,1,15))

class Bitmap :

    d = 0

    def __init__( self , n ) :

        self.n = [ i for i in str( n ) ]
        
        self.a , self.x , self.m = self.n , "" , 1 

    def __str__( self ) :

        self.f( self.n ) 
                    
        return ""

    def f( self , x  ) :

        for i in range( 5 ) :

            for s in range( self.m ) :

                print( self.x*( ( 5-i )*self.m - s - 1 ) , end="" )

                for n , ch in enumerate( x ) :
                    
                    for t in range( 3 , -1 , -1 ) :

                        print( self.a[n]*self.m if ( bmap[ int(ch) ][i]>>t )%2 else " "*self.m  , end="" )

                    print( end=" " )

                print()

    def setsym( self , x ) :

        self.a = [ x for i in self.a ]

    def set_slant( self , a = d ) :

        Bitmap.d += 1

        self.x = " " if Bitmap.d%2 else ""

    def enlarge( self , m ) :

        self.m = m

if __name__ == "__main__" :

    num = Bitmap( 98456 )

    print( num )

    num.setsym( "#" )

    print( num , end="\n\n" )

    num.setsym( "O" )

    num.set_slant()

    num.enlarge(2)
    
    print( num , end="" )

   
