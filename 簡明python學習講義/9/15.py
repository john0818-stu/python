from math import *
from numpy import *

def main() :

    a , b , n = pi , pi/4 , 100

    global h 

    h = ( a - b ) / n

    isum = 1 + sqrt(2) #正解

    rsum , tsum , ssum = rintergral( f , a , b , n ) , tintergral( f , a , b , n ) , sintergral( f , a , b , n )

    print( "矩形積分法 {} 誤差值為 : {}".format( rsum , abs(isum - rsum) )   )

    print( "梯形積分法 {} 誤差值為 : {}".format( tsum , abs(isum - tsum) )   )

    print( "Simpson積分法 {} 誤差值為 : {}".format( ssum , abs(isum - ssum) )   )

def f(x) :

    return abs( sin(x) - cos(x) )

def rintergral( f , a , b , n ) :

    ts = linspace( b , a , n + 1 )
    
    ans = sum( f(ts)[:-1] )*h
               
    return ans

def tintergral( f , a , b , n ) :

    ts = linspace( b , a , n + 1 )

    ans = h*( f(a) + f(b) + 2*sum( f(ts)[1:-1] ) )/2

    return ans

def sintergral( f , a , b , n ) :

    ts = linspace( b , a , n + 1 )

    ans = h*( f(a) + f(b) + 4*sum( f(ts[1:-1:2]) ) + 2*sum( f(ts[2:-1:2]) ) )/3
    
    return ans
    
main()
