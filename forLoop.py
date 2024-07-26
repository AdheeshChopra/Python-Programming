num = [1,2,3,4,5]

for val in num :
    print(val)

veggies = ["potato", "tomato", "onion", "brinjal", "ladyfinger", "cucumber"]

for val in veggies :
    print(val)


tup = (1,2,3,4,2,8,9)

for num in tup :
    print(num)


str = "Adheesh Chopra"

for char in str :
    if(char == 'o'):
        print("o Found")
        break
    print(char)
else :
    print("End")


# Question 1

nums = [1,4,9,16,25,36,49,64,81,100]

for el in nums :
    print(el)


# Question 2

nums = (1,4,9,16,25,36,49,64,81,100)
x = int(input("Enter the Number: "))
idx = 0
for el in nums :
    if(el==x):
        print("Number found at idx", idx)
    idx += 1


# Question 3

for i in range(1, 101) :
    print(i)


# Question 4

for i in range(100, 0, -1) :
    print(i)


# Question 5

n = int(input("Enter the number: "))
for i in range(1, 11) :
    print(i*n)


# Question 6

n = int(input("Enter the number: "))
sum = 0
i = 1
while i <= n :
    sum += i
    i += 1
print("Sum =", sum)


# Question 7

n = int(input("Enter the number: "))
fact = 1
i = 1
while i <= n :
    fact *= i
    i += 1
print("Factorial =", fact)

n = int(input("Enter the Number: "))
fact = 1
for i in range(1, n+1) :
    fact *= i
print("Factorial =", fact)