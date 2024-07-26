str1 = "This is a String."
str2 = 'Adheesh Chopra.'
str3 = '''This is also a String.'''

str4 = "This is a String.\nWe are creating it in Python." # next line
str5 = "This is a String.\tWe are creating it in Python." # tab space

print(str1)
print(str4)
print(str5)
print(str1+str2)

finalstring1 = str2+str3
print(finalstring1)

print(len(str3))

finalstring2 = str2 + " " + str3
print(len(finalstring2))