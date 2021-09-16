'''
def change_vals(a,b) :

    print(a)
    a = 10
    b.append(5)

foo , bar = 3 , [4,9]
change_vals( foo , bar )
print(foo,bar)
'''
'''
def inc_one( s , t) :

    s += 1
    t += 1
    return s , t
a , b = 2, 5
a , b = inc_one(a,b)
'''
'''
def change_lists(a,b):
    a = [3] # a == [3] , foo 不變
    b[0] = 5 # b[0] -> bar[0] 改成 5 

foo , bar = [9] , [2,7]
change_lists(foo,bar)
print(foo,bar)
'''

#大樂透
'''
from random import *

def lottery( n , best ) :
    while 1 :
        best.add( randint(1,49) )
        if len(best) == n : return

fset = set()
lottery( 6 , fset )
print( " ".join( map( str , sorted(fset) ) )  )
'''
