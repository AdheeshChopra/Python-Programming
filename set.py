collection1 = {1,2,2,2,"hello","world","world"}

print(collection1)
print(type(collection1))
print(len(collection1))


collection = set()

print(collection)
print(type(collection))

# Operations on set
# Add
collection.add(1)
collection.add(2)
collection.add("Adheesh")
collection.add((1,2,3)) # we can also add tuple in the set but cannot add lists

# Remove
collection.remove(1)

# Clear
collection.clear()

# POP
collection2 = {"hello", "Adheesh", "World", "Chopra"}
print(collection2.pop())


print(collection)


# Union and Intersection
set1 = {1,2,3}
set2 = {2,3,4}

print(set1)
print(set2)

print(set1.union(set2)) # union
print(set1.intersection(set2)) # intersection