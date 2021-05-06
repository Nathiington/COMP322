# Lists, tuples, dictionaries, sets AND ALSO STRINGS are all iterable objects.
# All these objects have a iter() method which is used to get an iterator

# a tuple is a data structure which is kind of similar to an array
# a tuple is immutable meaning it can't be changed or replaced
# a tuple is defined by ()
mytuple = ("Java", "Python", "PHP", "C++", "C#", "Dart", "Javascript", "HTML")
my_iterator = iter(mytuple)

# the next method gets the next value in the sequence
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))