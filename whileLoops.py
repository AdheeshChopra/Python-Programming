count = 1
while count<=5 :
    print("Hello")
    count += 1

i = 1
while i<=5 :
    print("Adheesh")
    i += 1


i = 1
while i<=5 :
    print(i)
    i += 1


i = 10
while i>=0 :
    print(i)
    i -= 1


# Question 1

i = 1
while i<=100 :
    print(i)
    i += 1


# Question 2

i = 100
while i >= 0 :
    print(i)
    i -= 1


# Question 3

i = 1
n = int(input("Enter the number: "))
while i <= 10 :
    print(i*n)
    i += 1


# Question 4

num = [1,4,9,16,25,36,49,64,81,100]

i = 1
while i <= 10 :
    print(i**2)
    i += 1

idx = 0
while idx < len(num) :
    print(num[idx])
    idx += 1


# Question 5

num = (1,4,9,16,25,36,49,64,81,100)
x = int(input("Enter the Number: "))
i = 0
while i < len(num) :
    if(num[i] == x) :
        print("Found")
    i += 1


# Break Statement

i = 1
while i<=5:
    print(i)
    if(i==3):
        break
    i+=1


num = (1,4,9,16,25,36,49,64,81,100)
x = int(input("Enter the Number: "))
i = 0
while i < len(num) :
    if(num[i] == x) :
        print("Found")
        break
    else :
        print("Not Found")
    i += 1


# Continue Statement

i=1
while i<=10 :
    if(i%2!=0):
        i+=1
        continue
    print(i)
    i += 1