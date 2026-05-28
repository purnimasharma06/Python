class Employee:
    a = 1
    
    @classmethod
    def show(cls):
        print(f"The class attribute of a is {cls.a}")

    @property #name is a function but make it feel like a property/attribute. It is used to access the function like an attribute.
    def name(self):
        return f"{self.fname} {self.lname}"
    
    @name.setter # This is used to set the value of the name property. It takes the value as an argument and then it splits the value into first name and last name and assigns them to fname and lname respectively.
    def name (self,value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]

e = Employee()
e.a = 45

e.name = "Harry Khan"
print(e.fname, e.lname)

e.show()