infile = open( "idioms.dat" , "r" , encoding = "utf8")        
    
x = [ "".join( ch.split() ) for ch in infile ]

nx = [ [ ord(d) for d in ch ] for ch in x ]

ans = {}

with open ( "strokes.dat" , "r" , encoding = "utf8" ) as infile :

    for ch in infile :

        cc0 , cc1 = ch.split()

        ans[ int( cc0[2:] , 16) ] = cc1
        
bb = []

cc = {}

for i , n in enumerate( nx ) :

    ss = [ int( ans[x] ) for x in n ]

    bb += [ss]

    cc[ ss[0] ] = ( [] if ss[0] not in cc else cc[ ss[0] ] ) + [ x[i] ]

for i in sorted( cc.items() , key = lambda i : i[0] ) :

    print( i[0] , "劃 :" )

    for ch in sorted( i[1] , key = lambda ch : bb[x.index( ch )][1] ) :

        print( ch )

    print()
        
