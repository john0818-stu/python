ans = {}

with open ( "wkdates.dat" , "r" , encoding="utf8" ) as infile :

    for ch in infile :

        x0 , x1 = ch.split(":")
        
        for x in x1.strip() :

            ans[x] =  x0.strip() + ( ans[x] if x in ans else "" )        

for ch in sorted( ans.items() , key = lambda x : -len( x[1] ) ) :

    print( ch[0] , "[{:>2}]".format( len( ch[1] ) ) , " ".join( sorted( ch[1] ) )  )
