'''
def test( x , List = [] ) :
    List += [x]
    return List

for i in range(10) :
    a = test( i )
    print( len(a) )
a = test( 1 , [] )

b = test( 1 )

c = test( 2 )

print( a == b )
print( a is b ) # is 判斷記憶體是否一樣

print( c )'''

def test( x , List = [] ) :

    List += [x]
    print( List , end=" " )
    if len( List ) > 2 :
        for i in range( len(List) ) :
            del List[0]
        print( "a" , end=" " )

    return List

for i in range(10) :
    a = test( i )
    print( a )
