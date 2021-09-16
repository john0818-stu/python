
n=4


a=3*n+4

for i in range (a) :

    for j in range(2*n-1):
        
        if j%2==0 : j=0
        else : j=1

        s=abs(j)
			
        f=n-s

        h=2*n+1-2*s

        w=4*(n-s)+1
			
        d=3*s
		
        if i<d:

            print(" "*w,end=" ")
				
        elif i<d+h:
            
            if i==d:
                
                print(" "*(d+h-i-1)+"*"+" "*(d+h-i-1),end=" ")

            else :
                            
                print(" "*(d+h-i-1)+"/"+"-"*(2*(i-d)-1)+"\\"+" "*(d+h-i-1),end=" ")
				
        elif i<d+h+f+1:
            
            if i==d+h+f :
                                
                print("|"+"="*(4*(n-s)-1)+"|",end=" ")
                
            elif i==d+h:

                print("|"+" "*(4*(n-s)-1)+"|",end=" ")
                
            elif i==d+h+1 :
                
                print("|"+" "*((n-s))+"|"+"¯"*(2*(n-s)-3)+"|"+" "*((n-s))+"|",end=" ")
                
            else :
                
                print("|"+" "*((n-s))+"|"+" "*(2*(n-s)-3)+"|"+" "*((n-s))+"|",end=" ")

        else :
                                
            print("II"+" "*(4*(n-s)-3)+"II",end=" ")

    print( )
   
