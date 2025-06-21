# How can we use tuples as dictionary keys? Why is this possible and is it good practice?
# Give an example.

# Because tuples never change, Python allows them to be used as keys in a dictionary — just like a name tag that stays the same.

# Tuples are like locked boxes: once you put things inside, you can't open and change them.
# Python likes this because it can remember and find the tuple key easily.

# Using tuples as dictionary keys can be good practice when:
# 1. You need to store data with multiple keys: Tuples can be used to represent multiple keys that uniquely identify a value.
# 2. You need to ensure immutability: Tuples ensure that the key values don't change accidentally.
# 3. You want to group 2+ pieces of info together (like city + date)

# Don’t use them when:
# You plan to change the values inside
# The tuple contains a list or something else that can change


# A dictionary that stores weather info using city and date
weather = {
    ('Lagos', 'June 15'): 'Sunny',
    ('Abuja', 'June 15'): 'Cloudy'
}

print(weather[('Lagos', 'June 15')])


weather[('Lagos', 'June 15')] = "Rainy"

print(weather[('Lagos', 'June 15')])

# You can’t change the key
# Because a tuple is immutable — once it's in the dictionary, its identity can't change.

# You can change the value
# You can update what the key points to, as many times as you like.

# Create a dictionary with tuple keys
student_grades = {
    ("John", "Math"): 85,
    ("John", "Science"): 90,
    ("Jane", "Math"): 95,
    ("Jane", "Science"): 88
}

# Access a value using a tuple key
print(student_grades[("John", "Math")])  # Output: 85
