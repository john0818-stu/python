poem = "春眠不覺曉處處聞啼鳥夜來風雨聲花落知多少"

s = range(5,11)

ms = max(s)

def main() :

    for i in range(ms):
            
        for j in range( len(s) ) :

            for t in range( f(j)-1 , -1 , -1 ) :

                if i < s[j] :

                    a = i + s[j]*t

                    print( ( poem[a] if a < len(poem) else "  " ) , end=" " )
                    
                else :

                    print( "  " ,end=" ")

            print( end="   " )

        print()

def f(j) :

    return len(poem) // s[j] + ( 1 if len(poem)%s[j] else 0 )

main()

