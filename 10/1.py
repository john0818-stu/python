import math

class Color :

    global ans

    nrgb = 3

    ans = {}

    def __init__( self , cname , r , g , b ) :

        self.cname = cname

        self.rgb = [ int(x) for x in [ r , g , b ] ]

    #輸出 16 進位表示
    def __str__( self ) :

        return ( "{:0>2x}"*Color.nrgb ).format( *( self.rgb ) ) 

    def name( self ) :

        return self.cname

    def red( self ) :

        return self.rgb[0]

    def green( self ) :

        return self.rgb[1]

    def blue( self ) :

        return self.rgb[1]

    #兩色顏色距離
    def distance_from( self , color ) :

        dr , dg , db = [ self.rgb[i] - color.rgb[i] for i in range( Color.nrgb ) ]

        ravg = ( self.red() + color.red() ) / 2

        return math.sqrt( 2*dr**2 + 4*dg**2 + 3*db**2 + ravg*( dr**2 - db**2 )/256 )

    def find_colse_colors( self , colors , dis ) :

        ans[ self.cname ] = []

        t = []
        
        for i in colors :

            v = "{:.1f}".format( self.distance_from( colors[ i ] ) )

            if 0 < float(v) <= dis :

                t += [ [ float(v) , i ] ]

        ans[ self.cname ] += sorted( t , key = lambda x : float( x[0] )  )
    
        return ans[ self.cname ] 
    
if __name__ == "__main__" :

    colors = {}

    with open ( "rgb.dat" ) as infile :

        for line in infile :

            n , *rgb = line.split()

            colors[n] = Color( n , *rgb )

    dis = 20
    
    for cname in colors :

        colors[ cname ].find_colse_colors( colors , dis )

    bb = {}

    for i in ans :

        if len( ans[i] ) :

            bb[i] = ans[i]
            
    e = 0

    for i in sorted( bb , key = lambda x : -len( bb[x] )*100 + float( bb[x][0][0] ) ) :

        e += 1

        print( "[{}] {}".format( e , i ) )

        for j , ch in enumerate( bb[i] ) :
        
            print( j+1 , "{:>4} {} {}".format( ch[0] ,colors[ ch[1] ] , ch[1] ) )

        if e == 3 :

            break

        

    
                
         

        

    

    

   
