class Morse_Code :

    def __init__( self ) :

        self.se = [ chr(i) for i in range( ord("a") , ord("z")+1 ) ]

        self.nn = [ ".-" , "-..." , "-.-." , "-.." , "." , "..-." , "--." , "...." , ".." , ".---" , "-.-" , ".-.." , "--" ,
                    "-." , "---" , ".--." , "--.-" , ".-." , "..." , "-" , "..-" , "...-" , ".--" , "-..-" , "-.--" , "--.."]
        
    def encode( self , foo ) :

        self.ans = []

        for x in foo :

            self.ans += [ [ x  , self.nn [ self.se.index( x.lower() ) ]  ] ]
            
        return " ".join( list( zip( *self.ans ) )[1] )

    def decode( self , bar ) :

        return "".join( list( zip( *self.ans ) )[0] )

if __name__ == "__main__" :

    morse = Morse_Code()

    while 1 :

        foo = input( "> " ).strip()

        bar = morse.encode( foo )

        print( bar , "-->" , morse.decode( bar ) )
