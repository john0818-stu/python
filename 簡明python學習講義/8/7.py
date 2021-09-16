n = input("詩人名字> ")

ans = {}

with open ('poems.db' , 'r' , encoding='utf8') as infile :
    
    for x in infile :

        x0 , x1 , *x2 = x.split()

        ans[x0] = [{ x1 : x2 }] + ( ans[x0] if x0 in ans else [] )

i = 1

for f in ans[n] :

    print( '[' + str(i) + "]" )

    i = i + 1

    for g in f.items() :

        print( g[0] + ":\n" + " ".join(g[1]) )
