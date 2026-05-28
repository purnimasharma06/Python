# Create a class (2-D vector) and use it to create another class representing a 3-D vector.
class TwoDVector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class ThreeDVector(TwoDVector):
    def __init__(self, x, y, z):
        super().__init__(x, y) # This will call the constructor of the parent class (TwoDVector) and then it will assign the values of x and y to the instance variables of the parent class. After that, it will assign the value of z to the instance variable of the child class (ThreeDVector).
        self.z = z

    def display(self):
        print(f"3D Vector: ({self.x}, {self.y}, {self.z})")

a = TwoDVector(1, 2)
a.show()
b = ThreeDVector(5, 2, 3)
b.show()