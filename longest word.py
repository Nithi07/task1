""" 7. (2)Write a python program to find the longest word in a given sentence"""

def long(words):
    a = words.split(' ')
    b = a[0:]
    d = []
    for i in b:
        c = len(i)
        d.append(c)
        if max(d) == c:
            print(i)

#output come stating to longest

message = input("Type here: ")
print(long(message))




