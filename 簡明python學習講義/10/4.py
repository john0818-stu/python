class Bucket :

    def __init__( self , n , name , fill = 0 ) :

        self.n ,  self.name = n , name
        
        if fill == True :
    
            self.fill = n

        else :

            self.fill = fill

    def __str__( self ) :

        return "{}:{}/{}".format( self.name , self.fill , self.n )

    # a 要到給 b
    def pour_to( self , a , b ) :

        if a.fill > b.n - b.fill :

            a.fill = a.fill - b.n + b.fill

            b.fill = b.n

        else :

            b.fill = b.fill + a.fill

            a.fill = 0

        return a , b

    def __rshift__( self , foo ) :
    
        return self.pour_to( self , foo )[0]

    def __lshift__( self , foo ) :
    
        return self.pour_to( foo , self )[1]
    
if __name__ == "__main__" :

    a , b , c = Bucket( 5 , "a" ) , Bucket( 3 , "b" ) , Bucket( 100 , "c" )

    f = Bucket( 100 , "f" , fill = True )

    f >> a >> b
    
    print( a , b , c , f , sep = " , " )

    a >> ( b >> c )
    
    print( a , b , c , f , sep = " , " )

    a >> ( b >> c )

    print( a , b , c , f , sep = " , " )

    ( a << f ) >> b

    print( a , b , c , f , sep = " , " )
