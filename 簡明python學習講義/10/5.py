class Score :

    def __init__( self , n ) :

        self.infile = open ( n , encoding = "utf8" )

        self.name , *self.s = zip( *[ line.split()[1:] for line in self.infile ] )

        self.grad = list( zip( *[ list( map( int , i ) ) for i in self.s ] ) )
        
    def find_score_between( self , a , b ) :

        self.ans = []

        for i , ch in enumerate( self.grad ) :

            x = sum( ch )/3

            if b > x > a :
 
                self.ans += [ [ self.name[i] , "{:>0.1f}".format(x) , str( self.grad[i] ) ] ] 

    def get_records( self , foo ) :

        s = []

        for i , ch in enumerate( sorted( self.ans , key = lambda x : -float(x[1]) ) ) :
            
            s += [ str(i+1) + " " + " ".join( x for x in ch ) ] 
            
        return "\n".join(s)

score = Score( 'score.dat' )
        
if __name__ == "__main__" :

    while 1 :

        a , b = [ int(x) for x in input( "> ").split() ]

        names = score.find_score_between( a, b )

        print( score.get_records( names ) )

