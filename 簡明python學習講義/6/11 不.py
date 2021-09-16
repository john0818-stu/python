pome1 = '''起看山色拂雲開，萬壑千重紫翠來。開戶鄭真芳草遙，閉關許瑾落花誰。
           醉醒只向書倉坐，醒醉惟從夢境回。塵世簪纓從不問，浮雲難上釣魚台。
           問誰花里掩松關，有客新從塵市還。來去燕當簾際舞，去來鷗在水濱間。
           人言行己在皆濁，吾謂持身良獨艱。濁世市交多惡客，但令無得近雲山。
           自憐衣褐老隆中，憶自童年倏作翁。湖海氣消年亦謝，煙霞情重癖難攻。
           謝山雲臥輸陶令，蔣迳花香勝鄭公。將寄愁懷對明月，只將琴拂弄三終。'''

pome = "".join( [ i for i in pome1 if i not in (" " , "\n" , "。" , "，" ) ] )

a = len(pome)

p = [ ["  "]*15 for i in range( 15 ) ]

dr ,dc  = [1,0,-1,0] , [0,-1,0,1] 

r , c = 0 , 14 #起點

d = 0 # 一開始方向

for i,ch in enumerate ( pome ) : #  i=下標  ch=裡面東西  enumerate函數
    
    p[ r ][ c ] = ch
    
    r += dr[ d ]
    
    c += dc[ d ]
    
    if r != c and r%2 == 0 and c%2 == 0 and c + r !=14 and (r != 2 or ( c != 10 and c != 4) ) and ( r != 12 or ( c != 10 and c != 4) ) and ( r != 4 or ( c != 2 and c != 12 ) ) and (r != 10 or ( c != 2 and c != 12 ) )  :

        d = d + 1

        d = d%4
        
    elif (r == c ==0 or r == c ==14 or (r == 0 and c ==14) or (r == 14 and c ==0) ) and r%2 ==0 and c%2 ==0  :

        d = d + 1

        d = d%4

for i in range (15) :

    for j in range (15) :

        print( p[ i ][ j ] , end="" )
        
    print()
        
   
        

    
    
    
    










