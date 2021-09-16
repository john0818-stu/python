from random import *

def main() :

    while 1 :

        n , m = eval( input("m,n> ") )

        a = [ [ str( randint(1,4) ) for j in range(m)] for i in range(n)]

        print( "A :" )

        for x in a :

            print( ' '.join(x) )

        print( "B :" )

        for x in zip(*a) :

            print( ' '.join(x) )

main()
