from typing_extensions import Self

class car:
    color=None
    topspeed=None
    def getinfo(self,x,y):
       self.color=x
       self.topspeed=y
       print("you have a,",self.color,"car with top speed",self.topspeed)  
    
    def calAvgSpeed(self,km,t):
     speed=km/t
     print("ypur speed is",speed)  
     
c1=car()  
c1.color="blue"
c1.topspeed=200
c1.getinfo()
    

     



