from random import *

def main() :

    n = int( input("> ") )

    jj = 1 + ( n + 2 ) + ( n + 1 ) +  ( 6 + 2*n ) + 1 + ( 7 + 2*n ) + ( 6 + 2*n ) + 1

    ii = 1 + 1 + ( 2 + n ) + ( 2 + n ) + ( 2 + n ) + 1 + 1

    for i in range(ii) :

        for j in range(jj) :

            if i == ii - 2 and j == 0 :

                print( "*" , end="" )

            elif i == ii - 1 and jj-3 <= j <= jj-1 :

                print( ":" , end="" )

            elif ( ii-3 <= i <= ii-2 and j == jj-3 ) or ( ii-3-n <= i <= ii-2 and j == jj-1 ) :

                print( "|" , end="" )

            else :

                print( "o" , end="" )

        print()

main()
