# CREATE A CLASS PROGRAMMER FOR STORING INFORMATION OF FEW PROGRAMMERS WORKING AT MICROSOFT

class Programmer:
    company = "Microsoft"
    def __init__(self, name, age, language):
        self.name = name
        self.age = age
        self.language = language

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Programming Language: {self.language}")
        print(f"Company: {self.company}")

programmer1 = Programmer("Alice", 30, "Python")
programmer1.display_info()
programmer2 = Programmer("Bob", 25, "JavaScript")
programmer2.display_info() 


# WRITE A CLASS CALCULATOR CAPABLE OF FINDING SQUARE CUBE AND SQUARE ROOT OF A NUMBER
class Calculator:
    def __init__(self, number):
        self.number = number

    def square(self):
        return self.number ** 2

    def cube(self):
        return self.number ** 3

    def square_root(self):
        return self.number ** 0.5

calc = Calculator(4)
print(f"Square of {calc.number} is {calc.square()}")
print(f"Cube of {calc.number} is {calc.cube()}")
print(f"Square root of {calc.number} is {calc.square_root()}")  