n = int( input("> ") )

for x in range( -n , n+1 ) :

        if x :

                for j in range(-n+1,n):

                
                        i = n - abs(x)

                        s = abs(j)

                        w = n - s

                        a = str(w) + " "

                        if i >= s:

                                print( a*w , end="" )

                        else:

                                print( " "*2*w , end="" )

                print()
print("end")
for i in range(2*n) :

        for j in range( n-1 , -n , -1 ) :

                a = n-abs(j)

                for s in range(a) :

                        print( ( str(a) if ( i + abs(j) < n + n  ) and ( i >= abs(j) ) else " " ) , end= " " )

        print()
