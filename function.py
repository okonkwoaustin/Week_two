#Define a function called person that takes in the following positional arguments 
# first_name, middle_name, last_name and the following keyword arguments sex, age. 
# The function should return all the data supplied. Remember to pass the appropriate 
# arguments when calling your function.

def person(first_name, middle_name, last_name, sex, age):
    return{
        "first_name": first_name,
        "middle_name": middle_name,
        "last_name": last_name,
        "sex": sex,
        "age": age
    }

result = person("John", "Doe", "Mike", sex="Male", age=50)

print(result)