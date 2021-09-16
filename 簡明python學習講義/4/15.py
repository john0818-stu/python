n = int( input( "> " ) )

vals = range( n , 0 , -1 )

for s in range ( n+1 , -n-2 , -1 ):
    
    print( " "*abs(s) , end="" )
    
    for val in vals :
        
        if  abs(s) == val + 1 or s == 0 :
            
            print( "*" if s else val , end=" " )
            
        elif abs(s) > val :
            
            print( " " , end=" " )
            
        elif s > 0 :
            
            print( "/" , end=" " )
            
        elif s < 0 :
            
            print( "\\" , end=" " )
            
    print()
    



