n = int ( input ( "> ") )

for a in range(n+1 , -n-1 ,-1):

    i = n - abs(a)

    if a :

        for j in range (-n+1,n):

            s = abs( abs( j ) - n + 1 )

            w = 2 * ( n - s )

            t = 2 * ( i  - s )

            if i < s :

                print( "|"*w , end="" )

            else:
                
                print( "|"*(n-1-i) + ( "\\" if a < 0 else "/" ) + " "*t + ( "/" if a < 0 else "\\" ) + "|"*(n-1-i) , end="" )

        print()
print(end="end\n")
for i in range( n , -n-1 , -1 ) :

    if i :
 
        for j in range( n - 1 , -n , -1 ) :

            a , b = abs(i) , abs(j)

            if b + 1 >= a and i > 0  :

                print( "|"*(a-1) + "/" + "  "*(abs(a-b-1)) + "\\" + "|"*(a-1) , end="" )

            elif b + 1 >= a and i < 0  :

                print( "|"*(a-1) + "\\" + "  "*(abs(a-b-1)) + "/" + "|"*(a-1) , end="" )

            else :

                print( ("||")*(b+1)  , end="" )

        print()
