from random import *

#x = "".join( [ x for x in line if x not in "？，。!；"] )#標點符號字體是全形

with open ( "poem2.0.dat" , "r" , encoding="utf8" ) as infile :

    data = [ po.strip() for po in infile if po != "\ufeff\n" ]
    
    poems = "".join( [ x if x != '' else '\n'  for x in data ] ).split()

    st = "？，。!；"
    
    poems = [ "".join( [ x if x not in st else "\n" for x in poem ] ).split()[::-1] for poem in poems ]
    

shuffle( poems )
pmax = max([ len(x[0]) for x in poems ])

for i in range( pmax ) :

    for poem in poems :

        for j in range( len(poem) ) :

            print( poem[j][i] if len( poem[j] ) > i else "　" , end=" " )
             
        print( end=" " )
    
    print()
