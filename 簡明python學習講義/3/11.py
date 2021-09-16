n = int( input("> ") )

for x in range(-n,n+1):

   if x != 0 :
      
      for j in range(-n+1,n):

         i = n - abs(x)
      
         s = abs(j)
       
         w = n - s
       
         a = str(w)
       
         if i == s :
          
            print( a*w , end="" )
          
         elif i > s :
          
            print( "-"*w , end="" )
          
         else:
          
            print( " "*w , end="" )
          
      print()

for i in range( n , -n-1 , -1 ) :

   if i :

      for j in range( n-1 , -n , -1 ) :

         a , b  = abs(i) , abs(j)

         if a == n - b  :

            print( str(n-b)*(n-b) , end="")

         elif a <= n - b :

            print( "-"*(n-b) , end="")
            
         else :

            print( " "*(n-b) ,end="" )

      print()
