# if
age = 21
if(age>=18):
    print("can vote")
    print("can drive")


# if-else
age = 45
if(age>=18):
    print("can vote")
    print("can drive")

else:
    print("can't vote")
    print("can't drive")


# if-elif
light = "Yellow"

if(light == "Red"):
    print("Stop")

elif(light == "Yellow"):
    print("Slow Down")

elif(light == "Green"):
    print("Go")

print("End")


# if-elif-else
light = "Yellow"

if(light == "Red"):
    print("Stop")

elif(light == "Yellow"):
    print("Slow Down")

elif(light == "Green"):
    print("Go")

else:
    print("Error")

print("End")


# nesting
age = 90
if(age>=18):

    if(age>=80):
        print("can't drive")
    
    else:
        print("can drive")

else:
    print("can't drive")