n = int( input("> " ) )

nums = [ [ 0 ]*n for i in range( n ) ]

s , t = 0 , 0 

ds , dt = [ 1 , 0 , - 1 ] , [ 1 , - 1 , 0 ]

m = n // 2

dir = 0

for i in range( int( ( 1 + n )*n / 2 ) ) : 
    
    nums[ s ][ t ]=i+1
    
    if ( s < m and (  2*t - s == -1 ) ) or ( s > m and ( s + t == n - 1 or 2*s - t == n - 1 ) ) :
        
        dir += 1
        
        dir = dir%3
        
    s += ds[ dir ]
    
    t += dt[ dir ]    

for i in range( n ):
    
    for j in range( i + 1 ):
        
        print('{:>3}'.format( nums[ i ][ j ] ) , end=" " )
        
    print()
        
