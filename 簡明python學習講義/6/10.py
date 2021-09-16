pome1 = ("寒泉漱玉清音好""好處深居近翠巒"
         "巒秀聳岩飛澗水""水邊松竹檜宜寒"
         "寒窗凈室親邀客""客待閒吟恣取歡"
         "歡宴聚陪終席喜""喜來歸興酒闌殘")

pome = ""

for x , ch in enumerate( pome1 ) :
    
    if pome1[x] != pome1[x-1] :
        
        pome += ch

p = [["  "]*13 for i in range(13)]

r , c = 6 , 12 #起點

a , b = 0 , 11

for i,ch in enumerate (pome) : #  i=下標  ch=裡面東西  enumerate函數
    
    p[ r ][ c ] = ch
 
    if r + c == 18 and r != 12 :

        r = r  -1 -2 * a

        c = c - 1

        a = a + 1

        continue
    
    if r == 12 and c == 6 :

        r = -1

        c = 5

    if r - c == 6 :

        r = r - b 

        c = c - 1
        
        b = b -2
              
    r = r + 2

    p[6][0] = pome[-1]
        
for i in range ( 13 ):
   
    print( "".join( p[ i ] ) ) 
        
    
    
    
    
    










