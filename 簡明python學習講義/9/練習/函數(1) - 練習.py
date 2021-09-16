def main() :

    while 1 :

        n = int(input("> "))

        for i in range(1,n+1) :

            a = [ x for x in range(1,i+1)]

            for j in powers(a,2) :

                print(j,end=" ")

            print()

def powers( a , b ) :

    return [ i**b for i in a ]

main()

