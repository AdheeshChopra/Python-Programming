# Question 1

# Let us say your expense for every month are listed below,
# January - 2200
# February - 2350
# March - 2600
# April - 2130
# May - 2190
# Create a list to store these monthly expenses and using that find out,

expenses = [2200, 2350, 2600, 2130, 2190]

# 1. In Feb, how many dollars you spent extra compare to January?
print("The extra dollars spent in February compare to January are:", expenses[1] - expenses[0])

# 2. Find out your total expense in first quarter (first three months) of the year.
print("The total expenses in first quater of the year:", expenses[0] + expenses[1] + expenses[2])

# 3. Find out if you spent exactly 2000 dollars in any month
print("Did I spent 200$ in any Month?", 200 in expenses)

# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
expenses.append(1980)
print("Expenses:", expenses)

# 5. You returned an item that you bought in a month of April and got a refund of 200$.
#    Make a correction to your monthly expense list based on this
expenses[3] = expenses[3] - 200
print("Expenses after 200$ refund:", expenses)


# Question 2

# You have a list of your favourite marvel super heros.
# heros=['spider man','thor','hulk','iron man','captain america']
# Using this find out,

heros=['spider man','thor','hulk','iron man','captain america']

# 1. Length of the list
print(len(heros))

# 2. Add 'black panther' at the end of this list
heros.append('black panthar')
print("Heros are:", heros)

# 3. You realize that you need to add 'black panther' after 'hulk', so remove it from the list first and then add it after 'hulk'
heros.remove('black panthar')
heros.insert(3, 'black panthar')
print("Heros:", heros)

# 4. Now you don't like thor and hulk because they get angry easily
#    So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
#    Do that with one line of code.
heros[1:3] = ['doctor strange']
print("Heros", heros)

# 5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)
heros.sort()
print("Heros:", heros)


# Question 3

# Create a list of all odd numbers between 1 and a max number. Max number is something you need to take from a user using input() function

max_num = int(input("Enter the maximum number: "))
odd_nos = []
for i in range(1, max_num):
    if i % 2 == 1:
        odd_nos.append(i)

print("Odd Numbers:", odd_nos)