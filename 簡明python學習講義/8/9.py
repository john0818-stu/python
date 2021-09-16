ans = {}

with open ('poems.db' , 'r' , encoding='utf8') as infile :

    a = [x for x in infile]

    for x in a :

        a0 , a1 , *a2 = x.split()

        for y in "".join(a2) :

            ans[y] = 1 + ( ans[y] if y in ans else 0 )
f = 0

for n in sorted( ans.items() , key = lambda n : -n[1] ) :

    print( "[{}] 出現於 {} 首詩中 :".format( n[0] , n[1]) )

    g = 0

    for x in a :

        if n[0] in x :

            aa = x.split()

            g = g + 1

            print( g , aa[0] , ":" , aa[1] )

    print()
    
    f =  f + 1

    if f == 3 :

        break
