from random import *

with open ( "poem2.0.dat" , "r" , encoding="utf8" ) as infile :

    poem , a = {} , 0

    for line in infile :
        
        if len(line) > 2 :

            x = "".join( [ x for x in line if x not in "？，。!；"] )#標點符號字體是全形

            poem[a] =  ( poem[a] if a in poem else "" )  + x.strip() 

        if line == "\n" :

            a = a + 1

s = [ poem[ randint(0,5) ] for i in range( 3 , 6 ) ] #隨機詩

r = [ randint(3,5) for x in range( len(s) ) ] #隨機列

c = [ int( len(s[i])/x+0.9 ) for i , x in enumerate(r) ]#我要的行

hh,vv,nw,ne,sw,se=chr(9472),chr(9474),chr(9484),chr(9488),chr(9492),chr(9496)
#('─','│','┌','┐','└','┘')

ss , dd = chr(9500) , chr(9508)
#('├', '┤')

for q in range( max(c)*2+1 ) :

    for j in range( len(c) ) :

        for t in range( r[j]-1 , -1 , -1 ) :            

            if q//2 < c[j] :
                
                if q%2 :

                    a = q//2 + c[j]*t
                    
                    print( ( vv + s[j][a] + vv if a < len(s[j]) else vv + " "*2 + vv )  , end="" )

                elif q == 0 :

                    print( nw + hh+hh + ne , end="" )

                elif q%2 == 0 :

                    print( ss + hh+hh + dd , end="" )

            elif int( q/2 + 0.5 ) == c[j] :

                    print( sw + hh+hh + se , end="" )

            else :

                print( " "*4 , end=""  )
                
        print( end="  " )

    print()

