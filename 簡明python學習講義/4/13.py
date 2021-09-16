from random import*

n = int( input( "> " ) )

a = [ i for i in range (5,-5,-1) if i]

nums = [ choice(a) for i in range(n) ]

for i in range(6,-7,-1):

    if i :

        for j in nums:
            
                if ( i < 0 and i == j - 1 ) or ( i > 0  and i == j + 1 ) :
                
                    print("{:>2}".format(j),end=" ")

                elif abs( i ) > abs( j ) :
                    
                     print( "{:>2}".format( "+" ) , end=" ")
                     
                elif ( j < 0 and i > 0 ) or (j > 0 and i < 0) :
                    
                     print( "{:>2}".format("a") , end=" ")
                                
                else:

                    print( '{:>2}'.format( "|" ) , end=" ")
            
    else :

        print( "="*n*3 , end="" )
    
        
            
    print()


    
