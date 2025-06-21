#Why use tuples instead of lists?

#Tuples are faster than list because they are immutable, which allows  python to optimize their storage and access.
#Tuples are hashable if they contain hasable oblects
#Tuples are great for dictionaries when we need to reference multiple elements. Can't use lists as keys because they are mutuable


#Define a tuple of names that is ten items in length.

names = ("Goat", "Dog", "Cow", "Monkey", "Ant", "Fish", "Cat", "Rat", "Hen", "Duck")


#Try to modify the seventh item in the tuple. What happens? Record your observations.

#names[6] = "Rabbit"

#Traceback (most recent call last):
#  File "C:/Users/User/Desktop/Python class studio3/Assignments/Week_two/Assignment_one.py", line 14, in <module>
#   names[6] = "Rabbit"
#TypeError: 'tuple' object does not support item assignment


#Write a for loop to print out each item in the tuple with their indexes.

#without specifying where the index should start from

print("#without specifying where the index should start from")

for index, name in enumerate(names):
    print(index, name)

print("#specifying the where the index should start")

#specifying the where the index should start

for index, name in enumerate(names, 1):
    print(index, name)
