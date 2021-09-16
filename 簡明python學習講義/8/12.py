ans = {}

c = "一二三四五"

with open ( "courses2.dat" , "r" , encoding="utf8" ) as infile :

    for x in infile :

        x0 , *x1 = x.split()

        for h in x1 :

            h0 , h1 = h.split(":")

            if h1.isdigit() :

                for i in h1 :

                    ans[h0,i] = ( ans[h0,i] if (h0,i) in ans else [] ) + [x0]
                    
            else :

                a0 , a1 = [ int(i) for i in h1.split("-") ]

                for i in range( a0 , a1  + 1 ) :
                    
                    ans[h0,str(i)] = ( ans[h0,str(i)] if ( h0,str(i) ) in ans else [] ) + [x0]       
       
for x in sorted( ans , key = (lambda x : int(str(c.index(x[0])) + x[1]) ) ) :

    if len(ans[x]) != 1 :

        print( "星期" + x[0] , "第" + x[1] + "節" , " ".join(ans[x]) )
