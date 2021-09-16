n = int( input ( "> " ) )

a = [ int(x) for x in str( n ) ]

h , l  = max( a ) , len( a )

for i in range (h,0,-1):
    
    for j in range (l):
        
        if a[ j ] :

            b = l - j 
            
            print("{:>2}".format( 10**(b-1) if i<= a[j] else " "*b   ) , end=" " )

                
    print()
    

