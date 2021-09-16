from random import *

animals = "兔牛馬羊狗貓"

ans = set()

while 1 :

    ani = [ x for x in animals ]

    while 1 :

        a = choice(ani)

        del ani[ani.index(a)]

        if len(ani) == 2 :

            break

    ans.add( "".join( ani ) )

    if len( ans ) == 10 :

        break
i = 1

for ch in ans :

    print( "{:>2}".format(i) ,  ch  )

    i = i + 1
