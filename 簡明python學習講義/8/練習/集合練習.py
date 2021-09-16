#2個數字重複
"""
for i in range( 10, 100 ) :
    
    a = str(i)

    # a = 11 len(a) = 2 len(set(a)) = 1

    if len(a) != len( set(a) ) :

        print(i)
"""

# 3 個數字有 2 個以上重複
"""
for i in range( 100 , 1000 ) :

    a = str(i)

    if len( set(a) ) != len(a) :

        print(i)
"""

#找出不重複數字 , 重複
"""
p ='''山山遠隔半山塘，心樂歸山世已忘。
樓閣擁山疑閬苑，村莊作畫實滄浪。
漁歌侑醉新絲竹，禪榻留題舊廟堂。
山近蘇城三四里，山峰千百映山光。'''
p = "".join( [ i for i in p if i not in "。， \n" ] )
print(len(p)) #不重複數字
print( len( set(p) ) ) #重複數字
"""

#產生 6 個 [ 1 , 49 ] 號碼
"""
from random import *

x = set()

while 1 :

    x.add( randint(1,49) )

    if len(x) == 6 :

        break

print( " ".join( map( str , sorted(x) )  )  )
"""

#在[1,5] x [1,5] 中取10個點

"""
from random import *

a = set()

while 1 :

    aa = ( randint(1,5) , randint(1,5) )

    if aa not in a :

        a.add(aa)

        if len(a) == 10 :

            break

s = 0

for x , y in sorted(a) :

    if x > s and s :

        print()

    print("({}{})".format( x , y ) , end=" " ) 

    s = x
"""  

    
