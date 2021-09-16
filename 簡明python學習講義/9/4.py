from random import *

def main() :

    n = int(input("> "))

    a = rotaing_mat(n)

    print( "Rotaing Matrix :" , a )

def rotaing_mat(n) :
    
    ans = [[0 for i in range(n)] for j in range(n) ]

    r , c , d = 0 , 0 , 0

    dr , dc = [0,1,0,-1] , [1,0,-1,0]

    for i in range( 1 , n**2+1 ) :

        ans[r][c] = i

        if ( r - c == 1 and r <= n//2 ) or ( r + c == n-1 ) or ( r == c and r >= n//2 ) :

            d = d + 1

        r += dr[d%4]
    
        c += dc[d%4]

    return "\n" + "\n".join( [ "  ".join( [ "{:>2}".format( str(y) ) for y in x ] )  for x in ans ] )
    
main()
