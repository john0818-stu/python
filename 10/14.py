class Queue :

    def __init__( self ) :

        self.lis = []

    def __str__( self ) :

        s = self.lis

        return ">stack size : {}{}{}".format( len(s) , "\n" if s else "" ," ".join(s) )
 
    def push( self , i ) :

        self.lis += [i]
        
    def empty( self ) :

        return True if len( self.lis ) == 0 else False 

    def front( self ) :

        return self.lis[0]

    def pop( self ) :

        del self.lis[0]
    
    def pusharry( self , x ) :

        self.lis = list( map( str , x ) )    
    
if __name__ == "__main__" :

    foo = Queue()

    for i in range( 1 , 4 ) :

        foo.push( str(i)*i )

    print( foo )

    while not foo.empty() :

        print( foo.front() )

        foo.pop()

    print( foo )

    foo.pusharry( [ 6 , 7 , 8 ] )

    print( foo )
