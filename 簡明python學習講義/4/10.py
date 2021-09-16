from random import*

a , n = eval( input( "4位數字 , 次數 = "))

b = [ int(x) for x in str(a) ]

number =list( range( 1 , 10 ) )

print( "答案: " , a )

for i in range(n):
  
    print(i+1,end=". ")

    s , k = 0 , 0 

    num=()
    
    for j in range( len( b ) ) :
        
         num += ( choice( number ), )
        
    nums = tuple(num)
    
    for x in nums[:]:
        
        print( x , end="" )
        
    for t in range( len( b ) ) :
        
        if b[ t ] == nums[ t ] :
            
            s += 1
            
        else:
            
            k +=1
            
    print(" ",":"," ",s,"A",k,"B",sep="")
    
           
