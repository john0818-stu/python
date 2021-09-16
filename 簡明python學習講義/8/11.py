ans = {}

with open ( "courses.dat" , "r" , encoding="utf8" ) as infile :

    f = infile.readline().split()
    
    infile.readline()

    for line in infile :

        x = line.split(" ")

        if len( x ) > 1 :

            for i , ch in enumerate(x[1:]) :

                if ch not in "\u3000\n|" :

                    if ch not in ans : # x[0] 第幾節 , i 禮拜幾 , ch 課程

                        ans[ch] = { i : x[0] }

                    else :

                        ans[ch][i] = ( ans[ch][i] + x[0] ) if i in ans[ch] else x[0]

for x in  sorted( ans.items() , key = lambda x : abs( max( [ -int( str(i[0])+i[1][0] ) for i in x[1].items() ] ) ) ) :

    print( x[0] , end=" " )

    for y in sorted( x[1].items() ) :
        
        print( f[ y[0] ] + ":" + y[1] , end=" " )

    print()

    
