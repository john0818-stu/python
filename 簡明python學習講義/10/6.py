from math import *

class Toy_Car :

    def __init__( self , x , y , speed = 2 , dir = 0 ) :

        self.x , self.y , self.speed , self.dir = x , y , speed , dir

    def __str__( self ) :

        return "車子位置 ( {:0.1f} , {:0.1f} ), 朝向 {} 度方向".format( self.x , self.y , self.dir )

    def forward( self , time ) :

        self.x = self.x + self.speed*time

    def drive( self , time , angle ) :

        self.dir = self.dir + angle

        t = self.dir*pi/180

        s = self.speed*time

        self.x = self.x + cos(t)*s 

        self.y = self.y + sin(t)*s 
        
if __name__ == "__main__" :

    car = Toy_Car(  0 , 1 , speed = 2 , dir = 0 )

    car.forward(10)

    print( car )

    car.drive( 5 , 90 )

    print( car )

    car.drive( 15 , 90 )

    print( car )

    
        
