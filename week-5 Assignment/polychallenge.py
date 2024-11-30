# Create a program that includes animals or vehicles with the same action (like move()). 
# However, make each class define move() differently (for example, Car.move() prints "Driving" 🚗, while Plane.move() prints "Flying" ✈️)



class Vehicle:
    def __init__(self,name,speed):
        self.name=name
        self.speed=speed
        
    def move(self):
        print('Driving')   
    
    
    
class Plane:
    def __init__(self,name,speed):
        self.name=name
        self.speed=speed
        
    def move(self):
        print('Flying')       
    
    
car1=Vehicle('totyota',2000)  
plane1=Plane('BOEING',3999)
car1.move()
plane1.move()
  