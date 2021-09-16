while 1 :

        n = int ( input ( "> ") )

        for a in range ( n+1 , -n-1 ,-1) :

                i = n - abs(a)

                if a :
                        for j in range(-n+1,n):
                                
                                s=abs(j)
                                
                                h=n-s
                                
                                w=2*(n-abs(j))
                                
                                t=i-s
                                
                                if i < s :
                                        
                                        print( " "*w , end="" )
                                else :
                                        print( " "*(n-1-i) + ( "\\" if a < 0 else "/" ) + " "*2*t + ( "/" if a < 0 else "\\" ) + " "*(n-1-i) , end="" )
                        print()	
                
"""
print()
print("end")
s = 0
for i in range( n , -n-1 , -1  ) :

        if i :
                for j in range( n-1 , -n , -1 ) :

                        a , b = abs(i) , 2*n - 2*abs(j) 

                        if a <= b//2 and i > 0 :

                                print( "+"*(a-1) + "/" + " "*(b-i*2 ) + "\\" + "+"*(a-1) , end=""   )

                        elif a <= b//2 and i < 0 :

                                print( "+"*(a-1) + "\\" + " "*( b-a*2 ) + "/" + "+"*(a-1) , end=""   )

                        else :
                                print( "a"*(b) , end="" )

                print()
#"""
                                
