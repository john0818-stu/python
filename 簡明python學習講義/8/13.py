from random import *

x = 50000

print( 'n' , "次數" )

for n in range(3,10) :

    g = 0

    for i in range(x) :

        ans = set()

        a = "".join( [ "".join( [ chr(ord('a')+i) for i in range(n)] )  for i in range(10) ] )
        
        while len(ans) < n :

            ans.add(choice(a))
            
            g = g  + 1
            
    print(n,g/x)


        
