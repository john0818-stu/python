class Longtitude :

    def __init__( self , foo ) :

        self.n = foo

        self.a , self.b = map( int , foo.split( "w" if "w" in foo else "e" ) )

    def shift( self , i ) :

        ts = self.ew( foo )*( self.a*60 + self.b ) + 60*i

        t = abs( int( self.g(ts)/60 ) ) , abs( self.g(ts) )%60

        return "{}{}{}".format(t[0], self.f( self.g(ts) ) , t[1])

    def ew( self , x ) :#判斷 e == 1 , w == -1

        return 1 if "e" in x else -1

    def f( self , x ) :#判斷 -1 == w , e == 1

        return "w" if x < 0 else "e"

    def g( self , x ) :#判斷 ts 有沒有越界

        return -self.ew( self.f(x) )*2*180*60 + x if abs( x ) > 180*60 else x
    
if __name__ == "__main__" :

    while 1 :

        foo = input( "> " )

        bar = Longtitude( foo )

        for i in range( -2 , 3 ) :

            print( bar.shift( i*10 ) , end=" " )

        print( "\n" )



    
