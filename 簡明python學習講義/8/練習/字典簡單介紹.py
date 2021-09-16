nums = {} #字典

a = set() #集合
"""
nums["one"] = 1
nums["two"] = 2
nums["三"] = 3
nums[ 4 ] = "four"
nums[0,1] = "point one"

print(nums[4]) # == "four"
"""

#zip,dict
"""
a = dict( one = 1 , two = 2 , three = 3 )
b = dict( [ ( "one" , 1 ) , ( "two" , 2 ) , ( "three" , 3 ) ] )
b == dict( zip( ["one","two","three"] , [1,2,3] ) )
c = { "one":1 , "two":2 , "three":3 }
d = dict( zip( ["零","一","二","三","四","五","六","七","八","九",] , [ i for i in range(0,10)]) )
e = { chr(ord("a")+i) : chr( ord("A")+i) for i in range(26) }

ff = "零一二三四五六七八九"
f = { i : ch for i , ch in enumerate(ff) }
#print( a["one"] ) # == 1
#print( b["one"] ) # == 1 
#print( c["one"] ) # == 1
#print(d["零"]) # == 0
#print( e["c"] + e["a"] + e["t"] )
"""

#dict 增加資料 or 刪除資料
"""
a0 = "零一二三四五六七八九"
a = dict( zip( [ ch for ch in a0 ] , [ i for i in range(10) ] ) )
b0 , b = "abc" , "ABC"

#寫法一加
#for i , ch in enumerate(b0) :
#    a[ch] = b[i]

#寫法二加
#a.update( zip( [i for i in b0],[i for i in b] ) )

#刪
del a["一"]
print(a)
"""
#取出資料
"""
a0 = "零一二三四五六七八九"
a = dict( zip( [ ch for ch in a0 ] , [ i for i in range(10) ] ) )

b = [ k for k in a.keys() ]#==零一二...# 也可寫b = list(a.keys())
b1 = [ k for k in a ]#==零一二...# 也可寫 b1 = list(a)

c = [ k for k in a.values() ]#==0123...# 也可寫 c = list(a.values())

d = [ p for p in a.items() ] #==[('零', 0), ('一', 1), ('二', 2)...] # 也可寫 d = list(a.items())

d1 = [ p[0] for p in a.items() ]#==零一二... 
d2 = [ p[1] for p in a.items() ]#==0123...
"""
#使用 sotred
"""
foo = dict( dog = 30 , cat = 4 , horse = 9 , goat = 8 )

for i in sorted( foo.keys() , key= lambda x : ( len(x) , -foo[x]) ) :
# sorted( , ket = (要怎麼比) ) 由小到大
# lambda x : ( len(x) , -foo[x] ) 函數
    print(i,foo[i])
print()
"""
















