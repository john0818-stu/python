from random import *

math = ( ( 15 , 9 , 9 , 9 , 15 ),( 2 , 2 , 2 , 2 , 2 ),( 15 , 1 , 15 , 8 , 15 ) , ( 15 , 1 , 15 , 1 , 15 ) , ( 9 , 9 , 15 , 1 , 1 )
        ,( 15 , 8 , 15 , 1 , 15),( 15 , 8 , 15, 9 , 15),( 15, 1 , 2 , 2 , 2 ),( 15 , 9 , 15 , 9 , 15 ) , ( 15 , 9 , 15 , 9 , 15 ) )

def main() :

    while 1 :

        n = int( input("> ") )

        s = randint(0,3)

        for i in range( 8 ) :

            for j in range( 3 , -1 , -1 ) :

                print( n if s <= i <= 4 + s and ( math[n][ i - s ] >> j )%2  else "-" , end="" )

            print()
            
main()

                
    
