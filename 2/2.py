for i in range (2,100) :
    
    print( i , "=" , end="" , sep="")
    
    for j in range (2,100) :
        
         while  i % j == 0 :
             
            print( j , end="" , sep="" )
            
            i = i // j
            
            if i > 1 :
                
                print( "x" , end="" , sep="" )
                
            else :
                
                break
            
    print()

    
