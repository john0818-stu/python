import random

lis = [ i for i in range(4) ]

print( random.choice( lis ) )


print( random.choices( lis , k = 3 ) )  #重複
print( random.sample( lis , k = 3 ) )  #不重複
