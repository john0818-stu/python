ans = {}

with open ( "cbitmap.dat" , "r" , encoding="utf8" ) as infile :
    
    for ch in infile :

        a , *x = ch.split()
        
        nx = [int(h,16) for h in x ]

        f = 0

        for r in range( len(nx) ) :

            for c in range( len(nx) , -1 , -1 ) :
	
                if nx[r] & ( 1 << c ) :

                       f = f + 1
                       
        ans[a] = f

for i in sorted( ans.items() , key = lambda i : i[1] ) :

    print( i[0] , i[1] )


