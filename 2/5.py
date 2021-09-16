for i in range(1,10):
    
    for t in range (4):
        
        for j in range(1,10):
            
            if t == 0 :
                
                print( " "*2 , j , end=" " , sep="" )
                
            if t == 1 :
                
                print( "x" , " " , i , end=" " , sep="" )
                
            if t == 2 :
                
                print( "-"*3 , end=" " )
                
            if t == 3 :
                
                print( "{:>3}".format(i*j) , end=" " )
                
        print()

    print()
        
    

