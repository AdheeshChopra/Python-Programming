# HOW TO READ A FILE
f = open("demo.txt", "r")
data = f.read() # reads entire file
print(data)

line1 = f.readline() # reads one line at a time
print(line1)

line2 = f.readline()
print(line2)
f.close()


# HOW TO WRITE IN A FILE
f = open("demo.txt", "w")
f.write("I want to learn JavaScript tommorow.")
f.close()


# HOW TO APPEND THE DATA
f = open("demo.txt", "a")
f.write("\nAfter that NodeJS.")
f.close()


# HOW READ AND OVERWRITE THE FILE
f = open("demo.txt", "r+")
f.write("abc")
print(f.read())
f.close()


# HOW TO READ AND WRITE OR TRUNKATE THE FILE
f = open("demo.txt", "w+")
print(f.read())
f.write("abc")
f.close()


# HOW TO WRITE AT THE END OF THE FILE
f = open("demo.txt", "a+")
print(f.read())
f.write("abc")
f.close()


# WITH SYNTAX
with open("demo.txt", "r") as f:
    data = f.read()
    print(data)

with open("demo.txt", "w") as f:
    data = f.write("new data")


# DELETING A FILE
import os
os.remove("sample.txt")