#-------------------------------------------------------------------------#
#Exercises with lists
#-------------------------------------------------------------------------#
#1. Create a list named "l" with the following values ([1, 4, 9, 10, 23]). Using the Python
#documentation about lists (https://docs.python.org/3.5/tutorial/introduction.
#html#lists) solve the following exercises:
#1. Using list slicing get the sublists [4, 9] and [10, 23].
#2. Append the value 90 to the end of the list "l". Check the difference between list
#concatenation and the "append" method.
#3. Calculate the average value of all values on the list. You can use the "sum" and
#"len" functions.
#4. Remove the sublist [4, 9].

l=[1, 4, 9, 10, 23]

print(l[1:3]) # Output [4, 9]

print(l[-2:]) # Output [10, 23]

l.append(90)
print(l) # [1, 4, 9, 10, 23, 90]

print(l + [90]) # [1, 4, 9, 10, 23, 90, 90], but will not change the list

sum = 0
for x in l:
    sum = sum + x

print(l)
print("Total : ", sum, " Length : ", len(l), " Avg : ", sum / len(l))

l[1:3] = []
print("Removing [4, 9]", l)