from math import *
from numpy import *

def main() :

    global a , b

    a , b = 0 , 1

    print( d( f , g ) )

def d( f , g ) :

    ts = linspace( b , a , 5000  )

    ans = sqrt(  ( integral( s , b , a ) )**2 )

    return ans

def f(x) :

    return x

def g( x ) :
               
    return x**2

def s(x) :

    return f(x) - g(x)

def integral( s , b , a , n = 5000 ) :

    h = ( b - a )/n

    ts = linspace( b , a , n+1 )

    ans = 0

    for i , ch in enumerate( ts[:-1] ) :

        ans += h*( ch + ts[i+1] )/2

    return ans

main()

    
