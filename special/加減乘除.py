n = input( ">" )

bmap=((15,9,9,9,15),(2,2,2,2,2),(15,1,15,8,15),(15,1,15,1,15),(9,9,15,1,1),(15,8,15,1,15),(15,8,15,9,15),(15,1,1,1,1),(15,9,15,9,15),(15,9,15,1,15))

#dd : + , * , / , =   

dd = ( ( 2 , 2 , 7 , 2 , 2 ) , ( 0 , 0 , 7 , 0 , 0 ) , ( 9 , 6 , 6 , 6 , 9  ) ,  ( 2 , 0 , 7 , 0, 2 ) , ( 0 , 7 , 0 , 7 , 0 ) )

if "+" in n :  

    a , b = n.split( "+" )

if "-" in n : 

    a , b = n.split( "-" )

if "*" in n : 

    a , b = n.split( "*" )

if "/" in n : 

    a , b = n.split( "/" )

ans = int( eval(n) ) 

foo = n + "=" + str(ans)

for i in range(5):

    for f in foo :

        if f != " " : 

            for j in range( 3 , -1 , -1 ) :

                if f not in "+-*\/=" :

                    print( f if ( bmap[int(f)][i] >> j )%2 else " " , end="")

                elif f == "+" :

                    print( "+" if ( dd[0][i] >> j )%2 else " " , end="" )

                elif f == "-" :

                    print( "-" if ( dd[1][i] >> j )%2 else " " , end="" )

                elif f == "*" :

                    print( "*" if ( dd[2][i] >> j )%2 else " " , end="" )

                elif f == "/" :

                    print( "O" if ( dd[3][i] >> j )%2 else " " , end="" )

                else :

                    print( "=" if ( dd[4][i] >> j )%2 else " " , end="" )

            print( end=" " )

    print()
