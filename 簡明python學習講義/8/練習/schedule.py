
w , d = 8 , 5

wkclass = [ ["  "]*d for i in range(w) ]

c = "一二三四五"

c2n = { b : a for a , b in enumerate(c) }

with open ( "schedule.dat" , "r" , encoding = "utf8" ) as infile :

    for ch in infile :

        a , *time = ch.split()

        for p in time :

            x , y = p.split(":")

            for y0 in y :

                wkclass[int(y0)-1][c2n[x]] = a[0]

print( "   |" , " ".join(c) )

print( "-"*20 )

ii = 1

for i in range( w + 1) :

    if i == 4 :

        print( "-"*20 )

    else :
    
        print( ii , " |" , " ".join(wkclass[ii-1]) )

        ii = ii + 1


