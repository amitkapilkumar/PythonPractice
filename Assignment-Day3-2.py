#2. Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.

#Sample:  Suppose the following input is supplied to the program:
#without,hello,bag,world
#Then, the output should be:
#bag,hello,without,world

x = ""
while True:
    words=input("Enter comma separated words (Enter 'quit' to quit): ")
    if words == 'quit':
        break
    wordlist=words.split(",")
    wordlist.sort()
    s = ""
    for x in wordlist:
        s = s + x + ","
    print(s[0:len(s)-1])
