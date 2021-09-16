n = int( input("> ") )

a = 3*n + 2

for i in range(a):
        
        for j in range(n):
                
                for s in range(2):
           
                        s = abs(j)
                                        
                        f = n - s

                        h = 2*n + 1 - 2*s

                        w = 4*( n - s ) + 1
                                        
                        d = 3*s
                                        
                        if i < d :
                                                
                                print( "+"*w , end="" )
                                                
                        elif i < d + h :
                                            
                                print( " "*(d+h-i-1) + "*"*(2*(i-d)+1) + " "*(d+h-i-1) , end=" " )
                                                
                        elif i < d + h + f :
                                                
                                print( " "*(2*(n-s)) + "|" + " "*(2*(n-s)) , end=" " )

                        else :
                                                
                            print( "="*( 4 *( n - s ) + 1 ) + "=" , end="" )

        print( )

