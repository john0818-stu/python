n = int ( input ( "> ") )

k = 1

for i in range (1,n+1) :
        
	print ( str(i)+"!" , "=" , end="" , sep=" " )
	
	for j in range (1,i):
                
		print ( j , "x" , end="" , sep="" )
		
	k = k * i
	
	print ( i , "=" , k) 
	
