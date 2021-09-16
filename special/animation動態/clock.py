from numpy import *
import pylab
from matplotlib import animation
import datetime
import time

fig = pylab.figure() 

ts = linspace( 0 , 2*pi , 100 )

x , y = cos(ts) , sin(ts)

minute_ts = linspace( 0 , 2*pi , 61 )
for i , t in enumerate( minute_ts ) :

    if i%5 :
        pylab.arrow( cos(t) , sin(t) , -cos(t)*0.03 , -sin(t)*0.03  )

    else :
        if i%3 :
            pylab.arrow( cos(t) , sin(t) , -cos(t)*0.075 , -sin(t)*0.075 , color = "green" )
        else :
            pylab.arrow( cos(t) , sin(t) , -cos(t)*0.1 , -sin(t)*0.1 , color = "red" )
            
pylab.plot(x,y)
pylab.scatter( 0 , 0 , lw=3 , color="green" )
hour , minute , second = map( int , time.ctime().split()[-2].split(":") )

se, = pylab.plot( [0 , cos( -(second-15)*6*pi/180 )*0.9  ] , [ 0, sin( -(second-15)*6*pi/180  )*0.9 ] )
ho, = pylab.plot( [0 , cos( -(hour%12-3+(minute-15)/60)*30*pi/180 )*0.4 ] , [ 0, sin( -(hour%12-3+(minute-15)/60)*30*pi/180 )*0.4 ] )
mi, = pylab.plot( [0 , cos( -(minute-15)*6*pi/180  )*0.7 ] , [ 0, sin( -(minute-15)*6*pi/180  )*0.7 ] )

def update(i) :

    pylab.axis("off")
    
    hour , minute , second = map( int , time.ctime().split()[-2].split(":") )

    se.set_data( [0 , cos( -(second-15)*6*pi/180 )*0.9  ] , [ 0, sin( -(second-15)*6*pi/180  )*0.9 ] )
    ho.set_data( [0 , cos( -(hour%12-3+(minute-15)/60)*30*pi/180 )*0.4 ] , [ 0, sin( -(hour%12-3+(minute-15)/60)*30*pi/180 )*0.4 ] )
    mi.set_data( [0 , cos( -(minute-15)*6*pi/180  )*0.7 ] , [ 0, sin( -(minute-15)*6*pi/180  )*0.7 ] )
    print(second)
ani = animation.FuncAnimation( fig , update ,interval = 1000 )
pylab.axis("off")
pylab.show()

