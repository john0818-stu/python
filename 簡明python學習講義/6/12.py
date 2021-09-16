pome ='''春風和煦滿常山，芍藥天麻及牡丹。遠志去尋使君子，當歸何必找澤蘭。

         夏半端陽五月天，菖蒲制酒樂豐年。庭前幾多紅娘子，笑道檳榔應採蓮。

         秋菊開花遍地黃，一回雨露一回香。扶童便取國公酒，醉到天南星大光。

         冬來無處不防風，白紙糊窗重複重。待到雪消陽起石，戶懸門外白頭翁。'''

p = "".join( [ i for i in pome if i not in ( " " , "。" , "，" , "\n" ) ] )

v = [ [ ["  "]*7 for i in range(7) ] for i in range(4)]

r , c , x , a = 0 , 0 , 3 , 1

for i , ch in enumerate (p) :

    v[x][r][c] = ch

    r = r + 1

    c = c + 1

    if r == 7 :

        r = a

        c = 0

        a = a + 1

    if r == 7 and c == 0 :

        x = x - 1

        r , c , a = 0 , 0 , 1
    
            
for i in range (7) :

    print( " "*( 6 - i ) , end="" )

    for j in range(4) :

        for s in range(7) :

           print( v[j][i][s]  , end="" )

        print(" " , end="" )

    print()


    

    

    
