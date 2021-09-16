from random import *

math = ( ( 15 , 9 , 9 , 9 , 15 ),( 2 , 2 , 2 , 2 , 2 ),( 15 , 1 , 15 , 8 , 15 ) , ( 15 , 1 , 15 , 1 , 15 ) , ( 9 , 9 , 15 , 1 , 1 )
        ,( 15 , 8 , 15 , 1 , 15),( 15 , 8 , 15, 9 , 15),( 15, 1 , 2 , 2 , 2 ),( 15 , 9 , 15 , 9 , 15 ) , ( 15 , 9 , 15 , 9 , 15 ) )

def main() :

    while 1 :

        n = str( input("> ") )

        s = [ randint(0,5) for i in range( len(n) ) ]

        for i in range( 10 ) :

            print( "-" ,end="" )

            for d , ch in enumerate(n) :

                for j in range( 3 , -1 , -1 ) :

                    print( ch if s[d] <= i <= 4 + s[d] and ( math[int(ch)][ i - s[d] ] >> j )%2  else "-" , end="" )

                print(end="-")

            print()
            
main()

                
    
