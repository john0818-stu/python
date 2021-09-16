
num = '零一二三四五六七八九'
p1 , p2 =  [ '','十','百','千' ] , [ '','萬','億','兆']

while 1 :

 
    nstr = input("> ")
    try :
        
        n = [] 

        for i , ch in enumerate( nstr[::-1] ) :
            
            if i%4 == 0 : n += [ ch ] 
            
            else : n[-1] += ch  

        for i , ch in enumerate( n ) : 
            
            ch_num = ''
            s = 0 
            for j , x in enumerate( ch ) :

                if x=='0' and s == 0 :

                    s += 1

                    ch_num += '零'
                    
                elif x != '0' :

                    s = 0 

                    ch_num += p1[j] + ( '兩' if ( j > 1 or ( i==len(n)-1 and len(ch)==1 ) ) and x == '2' else num[ int(x) ])  
                       
            n[i] = p2[i] + ch_num.lstrip("零")

        if len(n) == 1 and 1 < len( n[0] ) <= 3 and '一' in n[0] :

            print( "".join(n)[::-1].lstrip("一") )
            
        elif len(n) == 1 and n[0] in [ '' , '一' ] :

            print( "零" if n[0] == "" else "一" )

        else :
 
            ans = [ ( "零" if len(i)==1 else i )  for i in n ]
            
            print( "零".join( " ".join( "".join( ans ).split("零") ).split() ) )
            
    except :

        continue



                
