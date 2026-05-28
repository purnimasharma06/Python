class Employee: 
    language = "Python" # This is a class attribute
    salary = 1200000

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod #by marking this method as static, this means we do not need anything from the class to run this method. We can directly call this method using the class name without creating an instance of the class.
    def greet():
        print("Good morning")


harry = Employee()
# harry.language = "JavaScript" # This is an instance attribute
harry.greet()
harry.getInfo()  # 1
# Employee.getInfo(harry) => this and 1 are same only the syntax is different. In 1, we are calling the method using the instance, and in the second one, we are calling the method using the class and passing the instance as an argument.
 