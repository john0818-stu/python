n = int( input( "> " ) )

bmap = ( 384 , 960 , 384 , 192 , 240 , 232 , 356 , 612 , 112 , 80 , 142 , 129 , 130 , 768 )

for i in range( 14 ) :
    
    for s in range( n ) :
        
        for j in range( 9 , -1 , -1 ) :
                
            print( "*" if ( bmap[ i ] & ( 1 << j ) ) else " ", end="" )
                
    print()


