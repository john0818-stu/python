ans = {}

with open ( "wdates.dat" , "r" , encoding="utf8" ) as infile :

    name , day = zip( *[ x.split()[1:] for x in infile ] )

for i, dd in enumerate(day) :

    j = 0
        
    for d in dd.split(",") :

        if d.isdigit() :

            j += 1

        else :

            j += 1 + abs( eval(d) )

    ans[ name[i] ] = j

for i , k in enumerate( sorted( ans.items() , key = lambda k : -k[1] ) ) :

    print( "{:>2} {} [{}] {} {}".format( i+1 , k[0] , k[1] , k[1]*1200 , day[i] ) )
