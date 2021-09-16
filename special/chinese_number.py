cnum = "零一二三四五六七八九"
num = "兆億萬 "
dnum = " 十百千"

while 1 :

    n = input( "> " ).strip()

    ans = ""
    
    ln = int( len( n )/4 + 0.99 )

    for i in range( ln-1 , -1 , -1 ) :

        t = n[::-1][i*4:(i+1)*4][::-1] 
        
        lt = len( t )

        if len( t.strip("0") ) == 0 : continue

        for j , nt in enumerate( t ) :

            g = cnum[ int(nt) ]

            x = lt - j 
            
            if nt == "0" :
        
                if len( t.rstrip( "0" ) ) == lt and t[ j-1 ] != "0" :

                    ans += "零"
                  
                if len( t.lstrip("0") ) != lt and ( t[ j- 1 ] == "0" and j ) and ans[-1] != "零":

                    ans += "零"
                   
            else :

                if nt == "1" and dnum[ x - 1 ] == "十" and len(n) == 2 :

                    ans += dnum[x-1].strip()
                   
                else :

                    ans += "兩" if ( x > 2 and g == "二" ) else g 
                  
                    ans += dnum[ x - 1 ].strip()
                    
        ans += num[ 3-i ].strip() if len( t.strip("0") ) else ""
       
    print( ans )

            
    
