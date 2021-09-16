from random import *

def main() :

    while 1 :

        n = int( input("數字進位> "))

        for x in range( 2,10 ) :

            print( "{} 進制 : {}".format( x , f(n,x) ))

def f( n , x ) :

    ans = []

    while n :

        a = n%x

        n = n//x

        ans = [str(a)] + ans    

    return "".join(ans)

main()
