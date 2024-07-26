def show(n):
    if(n==0):
        return
    print(n)
    show(n-1)

show(5)


n = int(input("Enter the number: "))

def fact(n):
    if(n == 0 or n == 1):
        return 1
    else:
        return n*fact(n-1)
print(fact(n))

fact(n)


# Question 1

n = int(input("Enter the Natural number: "))

def sum(n):
    if(n == 0):
        return 0
    return sum(n-1)+n

print(sum(n))


# Question 2

fruits = ["Mango", "Apple", "Orange", "Grapes", "Litchi", "Banana"]

def ele_list(list, idx = 0):
    if(idx == len(list)):
        return
    print(list[idx])
    ele_list(list, idx+1)

ele_list(fruits)