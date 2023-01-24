#Static Method
class sum:
    @staticmethod
    def getsum(*args):
        sum = 0
        for i in args:
            sum += i
        return sum
def main():
    print("Sum: ", sum.getsum(1,2,3,4,5))
main()
#returns 15

    #----------------------------------------------------------------------------------------------------#

#Static Variable
class Dog:

    total = 0

    def __init__(self, name="unknown"):
        self.name = name
        Dog.total += 1

    @staticmethod
    def getNumOfDogs():
        print("There are currently {} dogs".format(Dog.total))

def main():
    spot = Dog(" Spot")
    kim = Dog(" Kim")
    spot.getNumOfDogs()
main()

    #----------------------------------------------------------------------------------------------------#

#Static Variable 2
class dresses:
#                                #define
    total = 0
#                                   #initialize
    def __init__(self, name = "unknown"):
        self.name = name
        dresses.total += 1
#                                   #static method
    @staticmethod
    def dressCount():
        print("You have {} dresses".format(dresses.total))

def main():                     #create objects
    pink = dresses("Pink")
    pink.dressCount()
main()                          #call function

    #----------------------------------------------------------------------------------------------------#

#Static Variables3
class balls:
    
    total = 0
    
    def __init__(self, color = "unknown"):
        self.color = color 
        balls.total += 1
        
    @staticmethod
    def ballcount():
        print('There are {} balls in the basket'.format(balls.total))
def main():
    Red = balls("Red")
    Blue = balls("Blue")
    pink = balls("pink")
    pink.ballcount()
main()
    