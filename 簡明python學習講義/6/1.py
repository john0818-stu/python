while 1 : 
    a , b = "零一兩三四五六七八九","0十百千萬"

    n = input("> ")

    c = [ int( x ) for x in n ] # 數字
        
    # 中文數字

    for i,ch in enumerate (c) :
        
        if c[ i ] == c[ i - 1 ] == 0 : continue
        
        c[ i ] = a[ ch ]
            
    d = [ b[ i ] for i in range( len( n ) - 1 , - 1 , - 1 ) ]

    for i in range ( len(c) ) :

        if d[ i ] == "0" or c[ i ] == "零"  :

            d[ i ] = ""

        if  ( 0 < i < len(n) - 1 and c[ i ] == c[ i + 1 ] == "零" ) or ( c[ i ] == "零" and i == len(c)-1 ) or ( c[i] == "零" and i == 0 ) :

            c[ i ] =  ""

        c[i] = c[i] + d[i]

    for i in range ( len(n) ) :

        if c[i] == "兩十" or c[i] == "兩" :

            c[i] = "二" if len( c[i] ) < 2 else "二十"

    print( "".join( c ) )

   



    

   

    





    
    
    
    










