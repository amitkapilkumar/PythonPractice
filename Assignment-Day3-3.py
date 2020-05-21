#3.Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.

#Sample: Suppose the following input is supplied to the program:
#Hello world
#Practice makes perfect

#--->Then, the output should be:
#HELLO WORLD
#PRACTICE MAKES PERFECT

lines = []
while True:
    line=(input("Enter line (Enter 'quit' to quit): "))
    if line == 'quit':
        break
    else:
        lines.append(line)

for x in lines:
    print(x.upper())
