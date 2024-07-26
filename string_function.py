str = "I am a Coder"

str = str.capitalize()
print(str.endswith("r")) # true
print(str.capitalize()) # I am a Coder

str = str.capitalize()
print(str) # I am a Coder

print(str.replace("e" , "i")) # I am a Codir
print(str.replace("Coder" , "Programmer")) # I am a Programmer

print(str.find("a")) # 2

print(str.count("am")) # 1