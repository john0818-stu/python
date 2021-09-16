a = "一二三四五六日"

ans , nans = {} , {}

with open ( "wkdates.dat" , "r" , encoding="utf8" ) as infile :

    for ch in infile :

        x0 , x1 = ch.split( ":" )

        for x in x1.strip():

            ans[x] =  x0.strip() + ( ans[x] if x in ans else "" )

for x in a[::-1] :

    for y in a :

        if x != y :

            nans[ "".join([x,y]) ] = "".join( set(ans[x]) & set(ans[y]) )
        
for ch in nans.items() :

    print( ch[0] , ":" , " ".join( sorted(ch[1]) )  )
