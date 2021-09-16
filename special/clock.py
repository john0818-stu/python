import time

p = 0

bmap=((15,9,9,9,15),(2,2,2,2,2),(15,1,15,8,15),(15,1,15,1,15),(9,9,15,1,1),(15,8,15,1,15),(15,8,15,9,15),(15,1,2,2,2),(15,9,15,9,15),(15,9,15,1,15)) 

ff = 3

while 1 :
    
    s = time.asctime( time.localtime(time.time()) )

    d = s.split()[-2].split(":")

    if p != d :

        for i in range( 5 ) :

            for dd in range( ff ) :

                for f , x in enumerate( d ) :

                    if f :

                        print( " *"*ff if ( f == 1 and i in [1,3] ) else "  "*ff , end ="  " )

                    for xx in x :

                        for j in range( 3 , -1, -1 ) :
                    
                           print( str(int(xx))*ff if ( bmap[int(xx)][i] >> j )%2 else " "*ff , end="" )

                        print( end="  " )

                print( )

        print()

    p = d 
