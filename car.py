# %%
class Car():
    
    def __init__(self,fuel,firm,model,year):
        self.__myFuel = fuel
        self.__milage = 0
        self.__fuelDis = 16
        self.__myGear = 0
        self.__mySpeed = 0
        self.__maxSpeed = 100
        self.__maxGear = 6
        self.__myFirm = firm
        self.__myModel = model
        self.__myYear = year
    
    def addFuel(self,fuel):
        self.__myFuel += fuel

    def getMilage(self):
        return self.__milage
    
    def getFuel(self):
        return self.__myFuel

    def driveDis(self,distance):
        fueldis = distance/self.__fuelDis
        if self.__myFuel - fueldis > 0 :
            print ("There is enough fuel, you can Drive")
            self.__milage += distance
            self.__myFuel -= fueldis
        else:
            print ("Cannot Drive, not enough fuel")
    
    def startCar(self):
        if self.__myGear > 0:
            print ("You already started the car")
        elif self.__myFuel <= 0:
            print ("Not enough fuel, cannot start the car")
        else:
            self.__myGear = 0
        
    def startDrive(self):
        if self.__myGear > 1:
            print ("You already start driving")
        else:
            self.shiftUp()
    
    def shiftUp(self):
        if self.__myGear == self.__maxGear:
            print("Max Speed, cannot shift up")
        else:
            self.__myGear += 1  
            self.__mySpeed += 10
    
    def shiftDown(self):
        if self.__myGear == 1:
            self.stopDriving()
        elif self.__myGear == 0:
            print("you are in parking, cannot shift down")
        else:
            self.__myGear -= 1
            self.__mySpeed -= 10
    
    def stopDriving(self):
        self.__myGear = 0
        self.__mySpeed = 0

    def getSpeed(self):
        return self.__mySpeed

    def getGear(self):
        return self.__myGear
    
    def __str__(self):
        return self.__myFirm + ' ' + self.__myModel


# %%



