from abc import ABC, abstractmethod

class Absclass(ABC):

    def print(self, x):
        print("Passed Value:", x)

    #Abstract Method
    @abstractmethod
    def task(self):
        print("We are in Absclass task")

#Create subclass
class test(Absclass):
    def task(self):
        print("We are inside test_class task")

#Object of test class created
testObj = test()
testObj.task()
testObj.print(100)

o1 = Absclass()
o1.task()