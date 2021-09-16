
n =int(input("> "))

for i in range (n):
        
	print( "sum([1," + str(n-i) + "])=" , end=" ")
	
	for j in range (1,n-i):
                
		print( j , '+' , end="",sep="")
		
	print( n-i , '=' , ( 1+n-i ) * ( n-i ) // 2 )
	

	
	
