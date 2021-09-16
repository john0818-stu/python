x = [ i for i in range(10) ]
y = x #兩個一樣
x += ['a']
print( y )

a = x[:]  #複製
x += 'b'
print( a )


#====================================================================


fruits = [ 'apple' , 'mango' , 'watermelon' , 'banana' , 'pineapple' ]
#print( "fruits (before) :" , fruits )
for f in fruits[:] :

    if f == 'apple' :

        fruits.insert( 0 , f )
        """
        跑第0筆 fruits = [ 'apple' , 'mango' , 'watermelon' , 'banana' , 'pineapple' ]
        跑第1筆 fruits = [ 'apple' , 'mango' , 'watermelon' , 'banana' , 'pineapple' ]
        跑第2筆 fruits = [ 'apple' , 'mango' , 'watermelon' , 'banana' , 'pineapple' ]
        ...
        """

#print( "fruits (after) :" , fruits )

'''
fruits = [ 'apple' , 'mango' ]
print( "fruits (before) :" , fruits )
for f in fruits :

    if f == 'apple' :
        
        fruits.insert( 0 , f )
        print( f  , "跑不完" )
        """
        跑第0筆 fruits = [ 'apple' , 'mango' ]
        跑第1筆 fruits = [ 'apple' , 'apple' , 'mango' ]
        跑第2筆 fruits = [ 'apple' , 'apple' ,'apple' , 'mango' ]
        ...
        """

print( "fruits (after) :" , fruits )
'''
