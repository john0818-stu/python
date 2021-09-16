sdict = {}

with open( "strokes.dat" , "r" , encoding = "utf8" ) as infile :

    for x in infile :

        x0 , x1 = x.split()

        num = int( x0[2:] , 16 )

        sdict[num] = int(x1) 

while 1 :

    a = input("> ")

    i = 0

    for c in a :

        a0 = sdict[ ord(c) ]

        print( c + ":" + str(a0) , end="  " )

        i += a0

    print( "=" , i , end="\n\n" )
