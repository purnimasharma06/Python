class Student:

    # ================= CLASS VARIABLE / CLASS ATTRIBUTE =================
    school = "ABC School"
    # school belongs to the CLASS, not to one particular student
    # Therefore: class variable + class attribute


    # ================= CONSTRUCTOR =================
    def __init__(self, name, age, marks):

        # ================ INSTANCE VARIABLES =================
        self.name = name
        # self.name → instance variable
        # Each object gets its OWN name

        self.age = age
        # self.age → instance variable
        # Each object gets its OWN age

        self.marks = marks
        # self.marks → instance variable
        # Each object gets its OWN marks


    # ================= INSTANCE METHOD =================
    def display(self):
        # display() → instance method
        # It works with a particular object
        # It uses self

        print("Name:", self.name)
        print("Age:", self.age)
        print("Marks:", self.marks)
        print("School:", self.school)


    # ================= INSTANCE METHOD =================
    def result(self):
        # result() → instance method

        if self.marks >= 40:
            print(self.name, "has passed")
        else:
            print(self.name, "has failed")


    # ================= CLASS METHOD =================
    @classmethod
    def change_school(cls, new_school):
        # change_school() → class method
        # cls represents the CLASS
        # It changes the class variable

        cls.school = new_school


    # ================= STATIC METHOD =================
    @staticmethod
    def is_adult(age):
        # is_adult() → static method
        # It does NOT need self
        # It does NOT need cls
        # It is simply a helper function inside the class

        if age >= 18:
            return True
        else:
            return False


# ==========================================================
# CREATING OBJECTS
# ==========================================================

s1 = Student("Rahul", 20, 85)
# s1 → object / instance of Student

s2 = Student("Priya", 17, 92)
# s2 → another object / instance of Student


# ==========================================================
# INSTANCE ATTRIBUTES
# ==========================================================

print(s1.name)
# name → instance attribute of s1

print(s2.name)
# name → instance attribute of s2

# Output:
# Rahul
# Priya


# ==========================================================
# INSTANCE METHODS
# ==========================================================

s1.display()
# display() → instance method
# Works on s1

s2.display()
# display() → instance method
# Works on s2


s1.result()
# result() → instance method

s2.result()
# result() → instance method


# ==========================================================
# CLASS VARIABLE / CLASS ATTRIBUTE
# ==========================================================

print(Student.school)
# school → class variable / class attribute

print(s1.school)
# s1 can also access the class attribute

print(s2.school)
# s2 can also access the class attribute


# ==========================================================
# CLASS METHOD
# ==========================================================

Student.change_school("XYZ School")
# change_school() → class method
# cls refers to Student class

print(Student.school)
# XYZ School

print(s1.school)
# XYZ School

print(s2.school)
# XYZ School


# ==========================================================
# STATIC METHOD
# ==========================================================

print(Student.is_adult(20))
# is_adult() → static method
# No object required
# No self
# No cls

print(Student.is_adult(15))
# False