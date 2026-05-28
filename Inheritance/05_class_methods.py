class Employee:
    a = 1
    
    @classmethod # It only takes class as an argument and it can access the class attributes but it cannot access the instance attributes.
    def show(cls):
        print(f"The class attribute of a is {cls.a}")

e = Employee()
e.a = 45

e.show()