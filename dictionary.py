info = {
    "name" : "adheesh",
    "subjects" : ["python", "C", "Java"],
    "topics" : ("dict", "set"),
    "age" : 19,
    "is_adult" : True,
    "marks" : 95.0
}

print(info["name"])
print(info["age"])
print(info["topics"])


info["name"] = "Adheesh"
info["surname"] = "Chopra"

print(info)


null_dict = {}
null_dict["name"] = "Adheesh Chopra"
print(null_dict)


# Nested Dictionary
student = {
    "name" : "Adheesh Chopra",
    "subjects" : {
        "Phy" : 92,
        "Maths" : 98,
        "Chem" : 95
    }
}

print(student["subjects"]["Chem"])


# Operations performed on Dictionary
print(student.keys()) # Returns all the keys present in Dictionary
print(list(student.keys())) # Returns the Dictionary keys in the form of Lists

print(len(list(student.keys())))
print(len(student)) # Returns length or number of keys in the Dictionary


print(student.values()) # Returns all the values present in Dictionary
print(list(student.values())) # Returns the Dictionary values in the form of Lists


print(student.items()) # Returns all the keys and values in the form of tuples
print(list(student.items())) # Returns all the keys and values in the form of lists


print(student.get("name")) # Returns the key or value according to the "?"


student.update({"city" : "Jammu"}) # Update the existing Dictionary
print(student)

new_dict = {
    "city" : "Jammu",
    "age" : 19,
    "name" : "adheesh" # If we enter existing key name into new dictionary, it will update the existing one
}
student.update(new_dict) # Both methods are correct
print(student)