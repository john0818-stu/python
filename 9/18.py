import pylab

from numpy import *

from random import *

ts = linspace( 0 , 10*pi , 1000 )

tx = sin( ts )*( e**cos( ts ) - 2*cos( 4*ts ) - sin( ts / 12 )**5 )

ty = cos( ts )*( e**cos( ts ) - 2*cos( 4*ts ) - sin( ts / 12 )**5 )

def main() :

    for i in range(12) :

        tt = -i*30*pi/180
        
        rs , rc = sin(tt) , cos(tt)

        x = rs*tx - rc*ty + 14*cos(tt)

        y = rc*tx + rs*ty - 14*sin(tt)
        
        color = [ random() for i in range(3) ] + [0.8]
                
        pylab.fill( y , x , color = color  )

        pylab.plot( y , x , color = color[:3]  )

    pylab.axis("off")#顯示區域(前面加"off"關掉做標軸)

    pylab.show()

main()
            


    
        
    
