#-------------------------------------------------------------------------#
#Exercises with dictionaries
#- Use the python documentation at https://docs.python.org/3/library/stdtypes.
#html#mapping-types-dict to solve the following exercises.
#-------------------------------------------------------------------------#

#Take the following python dictionary:
#ages = {
#"Peter": 10,
#"Isabel": 11,
#"Anna": 9,
#"Thomas": 10,
#"Bob": 10,
#"Joseph": 11,
#"Maria": 12,
#"Gabriel": 10,
#}

#1. How many students are in the dictionary? Search for the "len" function.
#2. Implement a function that receives the "ages" dictionary as parameter and return
#the average age of the students. Traverse all items on the dictionary using the
#"items" method as above.
#3. Implement a function that receives the "ages" dictionary as parameter and returns
#the name of the oldest student.
#4. Implement a function that receives the "ages" dictionary and a number "n" and
#returns a new dict where each student is n years older. For instance, new_ages(ages,
#10) returns a copy of "ages" where each student is 10 years older.

def avgAge(dictionary):
    sum = 0
    for key,value in dictionary.items():
        sum = sum + value
    return sum / len(dictionary)

def oldestStudent(dictionary):
    max = 0
    name = []
    for key,value in dictionary.items():
        if value > max:
            max = value

    for key,value in dictionary.items():
        if value == max:
            name.append(key)

    return name

def addNToAges(dictionary, n):
    for key,value in dictionary.items():
        dictionary[key] = value + n

ages = {"Peter": 10, "Isabel": 11, "Anna": 9, "Thomas": 10, "Bob": 10, "Joseph": 11, "Maria": 12, "Gabriel": 10}

print(ages)

print("Total students ", len(ages)) # output 8

print("Average age of students", avgAge(ages)) # 10.375

print("Oldest student(s) ", oldestStudent(ages)) # ['Maria']

addNToAges(ages, 10) # adding 10 to each students age
print("After adding 10years to all students", ages)

