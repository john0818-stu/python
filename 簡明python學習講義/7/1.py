import sys 

with open ( "1.dat" , "w" ) as outfile :

    for i in sys.argv :
        
        outfile.write( i + " "  )

with open ( "1.dat" , "r" ) as infile :
    
    for i in infile :

        a = "".join( i.split()[1:] )   

        print( a + "=" + str( eval( a ) ) )

