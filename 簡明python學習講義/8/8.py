n = input("字> ")

n0 = "".join( n.split() )

with open ('poems.db' , 'r' , encoding='utf8') as infile :

    d = 1
    
    for x in infile :

        x0 = "".join( x.split() )

        if len( set(x0)&set(n0) ) == len(n0) :

            a0 , a1 , *a2 = x.split()

            s = 2*( len( "".join(a2) ) - len(a1) - len(a0) ) + len(a2) - 1

            print( "[{}]\n{}{}{}\n{}".format( d , a1 , " "*(s) , a0 , " ".join(a2) ) )

            d = d + 1

            
