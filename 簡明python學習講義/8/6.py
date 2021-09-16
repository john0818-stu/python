x = "鼠牛虎兔龍蛇馬羊猴雞狗豬"

ans = { ch : 0 for ch in x }

infile = open ( "zodiac.dat" , "r" , encoding="utf8" )

a = "".join( [ "".join( ch.split() ) for ch in infile ] )

for x in a :

    ans[x] = ans[x] + 1

for y in ans.items() :

    print( y[0] , y[1] ) 
