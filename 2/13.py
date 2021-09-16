n = int ( input ( "> ") )

for i in range ( 2*n-1 , -1 , -1 ) :
        
    for s in range ( 2 , -1 ,-1) :

        a = ( 3 - s ) * 2 * n if s else 2 * ( n + 2 )

        for j in range (a) :

            if  ( i < n and s== 2 ) or s==1 or ( s == 0 and i < n+2 ) :

                if i == j :

                    print( "/" , end="" )

                elif j + i == a-1 :

                    print( "\\" , end="" )

                elif j - i > 0 and j + i < a - 1 :

                    print( "_" , end="" )
                    
                else :
                    
                    print( " " , end="" )
                    
            else :

                print( " " , end="" )
                
    print()
 
for i in range(2*n) :

    for j in range(3) :

        if j == 0 :

            if i >= n :

                print( " "*(2*n-i-1) + "/" + "__"*(i-n) + "\\" + " "*(2*n-i-1) , end="" )

            else :

                print( "  "*n  , end="" )

        elif j == 1 :

            print( " "*(2*n-i-1) + "/" + "__"*(i) + "\\" + " "*(2*n-i-1) , end="" )

        else :

            if i >= 3*n//2 - n :

                a = 3*n//2 - n

                print( " "*(2*n-i-1) + "/" + "__"*(i-a) + "\\" + " "*(2*n-i-1) , end="" )

            else :

                print( "  "*n  , end="" )

            
    print()
