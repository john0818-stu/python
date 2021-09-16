with open ( "wdates.dat", "r" , encoding = "utf8") as infile :

        a ,b  = zip( *[ x.split()[1:] for x in infile ] )
        
for k , x in enumerate(b) :

        i = 0
        
        for c in x.split(',') :

                if c.isdigit() :

                        i = i + 1
                        
                else :

                        i += abs( eval(c) ) + 1

        print( "{:<3}{:>3} [{}] {}".format( k+1 , a[k] , i , b[k] ) )
        
