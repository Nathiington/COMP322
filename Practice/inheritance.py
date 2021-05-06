class Person:
    def __init__(self, name, age):
        self.age = age
        self.name = name

    def print_name(self):
        print("Name:", self.name)

    def print_age(self):
        print("Age:", self.age)


person1 = Person("Nathan Rankopo", 20)
person1.print_name()
person1.print_age()


# to create a child class you add the parent class in parenthesis as below
class Student(Person):
    # the pass keyword is used when you don't want to add any properties/methods to the class
    # pass
    #
    def __init__(self, name, age, student_id, uni):
        # declaring the super() init enables you to access all the properties and functions of the parent class
        super().__init__(name, age)
        self.student_id = student_id
        self.uni = uni

    def print_student_id(self):
        print("Student ID:", self.student_id)

    def print_uni(self):
        print("University:", self.uni)


person2 = Student("John Johns", 21, 1001, "BIUST")
person2.print_name()
person2.print_uni()
person2.print_student_id()





