# Question 1

with open("practice.txt", "w") as f:
    f.write("Hi Everyone\nwe are learning File I/O\nusing Java\nI like programming in Java.")


# Question 2

with open("practice.txt", "r") as f:
    data = f.read()
new_data = data.replace("Java", "Python")
print(new_data)

with open("practice.txt", "w") as f:
    f.write(new_data)


# Question 3

word = "learning"
with open("practice.txt", "r") as f:
    data = f.read()
    if(data.find(word) != -1):
        print("Found")
    else:
        print("Not Found")


# Question 4

def check_line():
    word = "learning"
    data = True
    line_no = 1
    with open("practice.txt", "r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
                return
            line_no += 1
    return -1

print(check_line())


# Question 5

count = 0
with open("practice.txt", "r") as f:
    data = f.read()
    print(data)

    num = data.split(",")
    for val in num:
        if(int(val)%2==0):
            count += 1
print(count)