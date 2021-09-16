from random import *
n = int( input("> ") )
a = [ (0b00100,0b11111,0b10101,0b11111,0b00100) , (0b00100,0b11111,0b00100,0b01010,0b10001)  ]
b = '中大'

c = -1

for x in range(n) :

    for i in range(5) :

        c = c + 1
        
        for s in range( -n+1 , n ) :

            for j in range(4,-1,-1) :
                
                if x >= abs(s) :
                    
                    aa = ( c - 5*abs(s) )//(n-abs(s))                   

                    print( ( b[0]*(n-abs(s)) if ( a[0][ aa ]>>j)%2 else "  "*(n-abs(s)) ) , end="" )
                    
                else :

                    print( "  "*(n-abs(s)),end="")

            print(end=" ")
                          
        print()
        
for x in range(n-1,-1,-1) :

    for i in range(5) :

        c = c + 1
        
        for s in range( -n+1 , n ) :

            for j in range(4,-1,-1) :
                
                if x >= abs(s) :
                    
                    aa =  ( c - 5*abs(s) )//(n-abs(s))-5         

                    print( ( b[1]*(n-abs(s)) if ( a[1][ aa ]>>j)%2 else "  "*(n-abs(s)) ) , end="" )
  
                else :

                    print( "  "*(n-abs(s)),end="")

            print(end=" ")
                          
        print()

