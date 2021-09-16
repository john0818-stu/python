while 1 :

    n = input("中央> ")

    nn = { x : 0 for x in n }
    
    with open ( "cbitmap.dat" , "r" , encoding="utf8" ) as infile :

        for ch in infile :

            a , *x = ch.split()

            if a in n :

                nx = [int(h,16) for h in x]

                nn[a] = nx

    for r in range( len(nx) ) :
        
        for x in nn.items() :

            for c in range( len(nx) , -1 , -1 ) :

                print( x[0] if ( x[1][r] >> c )%2 else "  " , end="" )

        print()
