n = int ( input ( "> ") )

hh,vv,nw,ne,sw,se=chr(9472),chr(9474),chr(9484),chr(9488),chr(9492),chr(9496)

for i in range (n) :
    
    for j in range (n) :
        
        if i==j and i<n/2 :
            
            print(nw,end="")
            
        elif i+j==n and i!=0 and i<n/2 :
            
            print(ne,end="")
            
        elif i+j==n-1 and i!=0 and i>=n/2:
            
            print(sw,end="")
            
        elif i==j and i>n/2:
            
            print(se,end="")
            
        elif (i>j and i+j<n) or (i<j and i+j>n):
            
            print(vv,end="")
            
        else:
            
            print(hh,end="")
            
    print()
    
