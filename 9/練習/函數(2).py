def prod( n , *args ) :

    p = n

    for x in args :

        p *= x

    return p

def psum( *args , a = 0 ) :

# psum(2,3) args = [2,3] , psum(2,a = 5 ) args = [2]

    p = 1

    for x in args :

        p *= x
        print(x)

    return p + a

def member( name , **rec ) :##兩個星星可以字典{}
#member('amy', age=10 , dog = 2 )
    print( name + ":" )

    for k in sorted( rec ) :

        print( k , ":" , rec[k] , end=" " )

    print( end="\n\n" if len(rec) else "\n" )

def member( name , *friends , **rec ):

    print( name , ":" , "".join(friends) , sep="" )
    
    for k in sorted( rec ) :

        print( k , ":" , rec[k] , sep="" , end="" )

    print( end="\n\n" if len(rec) else "\n" )


        
