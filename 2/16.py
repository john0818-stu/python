n = int ( input ( "> ") )

hh,vv,nw,ne,sw,se=chr(9472),chr(9474),chr(9484),chr(9488),chr(9492),chr(9496)

for i in range(2*n-1):
    
    for j in range(n):
        
        if i==j :
            
            print( nw + hh*(n-2) + ne , end="" )
            
        elif i==j+n-1:
            
            print( sw + hh*(n-2) + se , end="" )
            
        elif i>j and i<j+n-1:
            
            print(vv + hh*(n-2) + vv , end="")
            
        else:
            
            print( "  "*n,end="")
            
    print()
