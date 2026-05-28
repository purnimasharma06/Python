class Number:
    def __init__(self, n):
        self.n = n

    def __add__(self, num): # This is called operator overloading. It allows us to define the behavior of the + operator for our custom class. In this case, we are defining the behavior of the + operator for the Number class. When we use the + operator with two Number objects, it will call the __add__ method and pass the second Number object as an argument. The __add__ method will then return the sum of the n attributes of both Number objects.
        return self.n + num.n

n = Number(1)
m = Number(2)

print(n + m) # this doesn't work because we haven't defined the behavior of the + operator for the Number class. But after defining the __add__ method, we can use the + operator with Number objects and it will return the sum of their n attributes.
