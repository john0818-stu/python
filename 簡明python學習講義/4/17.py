n = int( input( "> ") )

nums = [ [ "  " ]*( 2*n - 1 ) for i in range( 2*n - 1 ) ]

s , t = 0 , n-1

ds , dt = [ 1 , 1 , -1 , -1 ] , [ 1 , -1 , - 1 , 1 ]

dir = 0

for i in range( n*n ):
    
    nums[ s ][ t ] = i + 1 
    
    if s == n - 1 or ( s < n - 1 and t == n - 2) or (s > n - 1 and t == n - 1 ) :
        
        dir += 1
        
        dir = dir%4
    
    t += dt[ dir ]
    
    s += ds[ dir ]
    
    
for i in range( 2*n - 1 ) :
    
    for j in range( 2*n - 1 ) : 
            
        print(nums[ i ][ j ] , end="" ) 
        
    print()
        
