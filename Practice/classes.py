class Person:
    # init acts as a constructor where we can pass arguments in the main function
    # self resembles the 'this' keyword in other languages
    # self parameter is a reference to the current instance of the class
    # self is also used to access variables that belongs to the class.
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # declaring object methods
    def print_name(self):
        print("My name is:", self.name)

    def print_age(self):
        print("My age is:", self.age)


# creating and instantiating Person object
person1 = Person("John", 21)
# this will display the memory size of the object in bytes
print(person1.__sizeof__())
# calling object methods
person1.print_name()
person1.print_age()
