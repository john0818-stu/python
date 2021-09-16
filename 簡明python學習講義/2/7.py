n = int ( input ( "> ") )

for i in range(n) :

    for j in range(2*n+1+2*(n-2)) :

        if i == j%(n+n-2) or i + j%(n+n-2) == n+n-2 :
            print( j+1 , end=" ")
        else :
            print(' ' , end=" " )
    print()
