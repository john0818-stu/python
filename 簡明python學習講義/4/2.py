n = int ( input ( "> ") )

nums=[[None]*n for i in range(n)]

for i in range (n):
    
    k = 0
    
    for j in range (n):
        
        if abs( i - j ) == k :
            
            nums[ i ][ j ] = k + 1 
            
            nums[ j ][ i ] = k + 1
            
            k = k + 1
            
for i in range (n):
    
    for j in range (n):
        
        print( "{}".format( nums[ i%n ][ j%n ] ) , end=" " )
        
    print()

