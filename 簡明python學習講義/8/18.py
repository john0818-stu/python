ans = {}

infile = open ( "idioms.dat" , "r" , encoding="utf8" )

a1 = [ "".join( x.split() ) for x in infile ]

a0 = [ x[0] for x in a1]

for x in a0 :

    ans[ x[0] ] = ( ans[ x[0] ] if x[0] in ans else 0 ) + 1

for x in sorted( ans.items() , key = lambda x : -x[1] ) :

    print( x[0] , x[1] )

    j = [ ch for i , ch in enumerate(a1) if x[0] == ch[0] ]

    for i in j :

        print( i , end= ( " " if j.index(i)%5 != 0 or j.index(i) == 0 else "\n" )  )
            
    print(end="\n\n")
    

    

        
    
