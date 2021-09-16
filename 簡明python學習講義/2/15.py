n = int ( input ( "> ") )

hh,vv,nw,ne,sw,se=chr(9472),chr(9474),chr(9484),chr(9488),chr(9492),chr(9496)

for i in range(n):
    
    for t in range(3):
        
        for j in range (n):
            
            if t==0:
                
                if i==j and i<n/2:
                    
                    print(nw,end="")
                    
                elif i+j==n and i!=0 and i<n/2:
                    
                    print(ne,end="")
                    
                elif i+j==n-1 and i!=0 and i>=n/2:
                    
                    print(sw,end="")
                    
                elif i==j and i>n/2:
                    
                    print(se,end="")
                    
                elif (i>j and i+j<n) or (i<j and i+j>n):
                    
                    print(vv,end="")
                    
                else:
                    
                    print(hh,end="")
                    
            elif t==1 and j==0 and i==0 :
                
                print(ne,end="")
                
                break
            
            elif t==1 and j==0 and i==n-1 :
                
                print(sw,end="")
                
                break
            
            elif t==1 and j==0  :
                
                print(vv,end="")
                
                break
            
            else :
                
                if i==j and i<n//2:
                    
                    print(nw,end="")
                    
                elif i+j==n-1 and i<n//2:
                    
                    print(ne,end="")
                    
                elif i+j==n-2 and i!=n-1 and i>=n//2:
                    
                    print(sw,end="")
                    
                elif i==j and i>=n//2:
                    
                    print(se,end="")
                    
                elif (i+j<=n-1 and j-i>=0) or (i-j>=1 and i+j>=n-1):
                    
                    print(hh,end="")
                    
                else:
                    
                    print(vv,end="")
	
    print()
