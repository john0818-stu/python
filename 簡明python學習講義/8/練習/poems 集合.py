
with open ( "poems.dat" , "r" , encoding = "utf8" ) as infile :

    for i , ch in enumerate(infile) :

        #poem = set( filter ( lambda x : x not in "，。" , ch.strip() ) )

        poem = set( i for i in ch if i not in "。，\n" )

        if i == 0 :

            word = poem
            
        else :

            word = word & poem

    print( " ".join( word) )
