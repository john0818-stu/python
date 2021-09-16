#"""
n = int( input( ">" ) )

for i in range( n ) :

    for s in range( 3 ) :

        print( " "*3*(n-i-1) , end="" )

        for t in range( n ) :

            for j in range( t + 1 ) :

                if n - i - 1 + j <= t :

                    print( str( i+t-n+2 )*5 , end=" "  )

                else :

                    print( " "*5 , end=" " )

            print( end=" " )

        print()
                    


#"""


"""
n = int ( input ( "> ") )

for t in range (n):

    for i in range (3):

        print( " "*3*(n-1-t) , end="" )

        for h in range (n) :
 
            b = abs( n - t - 1 - h ) + 1#每列有幾個
            
            a = ( h + 1 )#山高
            
            if   t >= n - a:
            
                for k in range (b):
                                    
                    b = abs( n - t + 2 - h ) #對應數字,寬度
        
                    print ( str( n - b )*5 , end=" " )
                    
                for j in range (n-t-1):
                
                    print( "-"*5 , end=" " )
                        
            else :
                
                b = abs ( n - t - 1 - h )#每列有幾個
            
                for k in range (b):
                    
                    for i in range (5) :
                        
                        print ( "a" , end="")

                    print (end=" ")

        print()

#"""
        
"""
n = int( input("> ") )

for i in range( n ) :

    for j in range( 3 ) :

        print( " "*( n - i - 1 )*3 , end = "" )
 
        for s in range( n ) :

            for t in range( s + 1 ) :

                if i - t - n + s + 1 >= 0 :

                    print( str( s + 2 - n + i )*5 , end=" " )

                else :

                    print( " "*5 , end=" " )
            
        print()
        
#"""
