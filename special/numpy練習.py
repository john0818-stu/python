import numpy as np
import random as rd

a = np.array([ [ 1 for x in range(3) ] for x in range(2) ])
b = np.array([ [ rd.randint(1,9) for x in range(3) ] for x in range(2) ])

#==========
# np -> list
# list -> np
#==========

print("------------np -> list-----------------------")
print( repr( b ) )
print( repr( a ) )
print( "np -> list" )
print( a.tolist() )
print( b.tolist() )


print("-----------shape------------------------")
#shape
print( b.shape , end="\n\n" )

print("-----------reshape------------------------")
#reshape
#改變維度(-1表示自動計算) 但不是transpose
c = b.reshape( -1 , 3 , 2 )
d = b.reshape( -1 )
print(c)
print(d)

print("---------transpose--------------------------")
#transpose
new = np.transpose(b)
print(new)

print("-----------dtype------------------------")
#dtype
print( type(b) )
print( b.dtype )#int32 32表示32位元

print("------------astype-----------------------")
#astype
print( b.astype('int64') )

print("------------ndim-----------------------")
#ndim
print( b.shape )
print( b.ndim )
print( len(b.shape) )



