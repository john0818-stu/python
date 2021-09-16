from random import *

class Intrange :

    def __init__( self , n ) :

        self.num0 , self.num1 = self.f( n )

    def get_num( self ) :

        return randint( self.num0 , self.num1 )

    def f( self , n ) :

        s = n[1:-1]

        if "," in s :

            return int( s[0] ) , int( s[2:] )

        else :
            
            return 10**( int( s[0] )-1 ) , -1 + 10**int( s[2:] if ":" in s else s[0] )

if __name__ == "__main__" :

    while 1 :

        num = input( "> " )

        foo = Intrange( num )

        for i in range( 10 ) :

            print( foo.get_num() , end = " " )

        print("\n")
