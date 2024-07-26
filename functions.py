def calculate_sum(a, b):
    sum = a + b
    print(sum)
    return sum

calculate_sum(34, 56)
calculate_sum(23, 45)


def cal_sum(a, b):
    return a+b

sum = cal_sum(6, 4)
print(sum)


def hello():
    print("Hello World")

hello()
hello()
hello()
hello()
hello()


# Average of three numbers

def av(a, b, c):
    return (a+b+c)/3

average = av(3, 6, 9)
print(average)


# Question 1

cities = ["Delhi", "Gurgaon", "Jammu", "Noida", "Pune", "Mumbai", "Chennai"]
heroes = ["Thor", "Ironman", "Hulk", "Captain America", "Antman", "Wanda", "Batman"]

def print_len(list):
    print(len(list))

print_len(cities)
print_len(heroes)


# Question 2

heroes = ["Thor", "Ironman", "Hulk", "Captain America", "Antman", "Wanda", "Batman"]

def print_list(list):
    for item in list:
        print(item, end = " ")

print_list(heroes)


# Question 3

n = int(input("Enter the number: "))

def cal_fact(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print(fact)

cal_fact(n)


# Question 4

n = int(input("Enter the amount($): "))

def usd_inr(n):
    inr = 83*n
    print("The amount in INR is", inr)

usd_inr(n)


# Question 5

n = int(input("Enter the number: "))

def odd_even(n):
    if(n%2==0):
        print("Even")
    else:
        print("Odd")

odd_even(n)