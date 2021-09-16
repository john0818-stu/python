a = { 1 , 2 , 3 , 4  }
a.clear() #清除集合

a = set( range(1,5) )
a.clear() #清除集合

a = [ 3 , 2, 9 , 2, 9]
a = set(a) #集合所以不重複
a = list(a) #幹第七章忘了用你
#print(a)
a.clear()#清除集合


a = [ 1 , 2 , 3 , 4 ]
a = set(a)
b = a.copy() #複製 a 所以我刪除 b , a 還是會留著 ，兩個存放 id() 不同
b = a #兩個存放 id() 相同
b.clear()#清除集合
#print(a,b)
a.clear()#清除集合

a = set( [1,2,3,4,5,7,1,2,3,4,79,5] )

a.add("c") #將 c 放入 a 裡
a.remove("c") #將 c 刪除 如果裡面沒有 c "會"錯誤
a.discard("c") #將 c 刪除 如果裡面沒有 c "不會" 錯誤
len(a) #集合個數
#print(a)

a = set( i for i in range(15) )

a = set( [ 1 , 2, 5 , 9 ,15 ,19, 21,2 ] )

#for i in a :
    #a.discard(i)#不能跑
    #a.add( str( int(i) + 1 ) )#不能跑
#print(a)

"""
a , b , c= {1,2,3} , {2,4,6} , {2}
print( a&b )
print( a|b )
print( a - b )
print( a^b ) #重複的刪掉
2 in a == True
5 in a == False
print( a == b ) #False
print( a >= c ) #包含嗎True
print( a <= c ) #包含嗎False
print( a > a ) #包含但不等於 False
print( a.isdisjoint(b) )  # a 與 b "沒" 交集對嗎？
"""
# 凍集合不能更改裡面內容

a = set( [ 1 , 2, 3 , 4 , 665 , 54 , 8 , 6848 , "a" ] )

b = frozenset(a)

