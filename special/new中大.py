n = int( input("> ") )

lis = [ [0b00100,0b11111,0b10101,0b11111,0b00100] , [0b00100,0b11111,0b00100,0b01010,0b10001][::-1]  ]


for h in range( n*5 , -n*5 , -1 ) :
    
    i = n*5 - abs(h) -1 
    
    for s in range( -n+1 , n ) :

        for j in range(4,-1,-1) :
                
            if i >= 5*abs(s):

                a = (i-5*abs(s))//( n-abs(s) )
                
                b , c  = ( 0 , '中' ) if h > 0 else ( 1 , '大' ) 

                x = n - abs(s)
                
                print( c*x if ( lis[b][a]>>j )%2 else "  "*x , end="" )
                    
            else :

                print( "  "*( n - abs(s)) , end="")

        print(end=" ")
                          
    print()
   
