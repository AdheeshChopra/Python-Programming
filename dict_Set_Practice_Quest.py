# Question 1

dict = {
    "table" : ["a piece of furniture", "list of facts and figures"],
    "cat" : "a small animal"
}
print(dict)


# Question 2

subjects = {
    "python", "java", "C++", "python", "javascript", "java", "pyhton", "java", "C++", "C"
}

print(len(subjects))


# Question 3

marks = {}

x = int(input("Enter the marks of Physics: "))
marks.update({"Physics" : x})

y = int(input("Enter the marks of Chemistry: "))
marks.update({"chemistry" : y})

z = int(input("Enter the marks of Maths: "))
marks.update({"Maths" : z})

print(marks)


# Question 4

# Method 1
values = {9, "9.0"}

# Method 2
values = {
    ("float", 9.0),
    ("int", 9)
}

print(values)