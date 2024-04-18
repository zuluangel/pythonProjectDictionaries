# print("Please write anything")
# x = input()
# y = input()
# sayHello = "This is a new starting"
# print(sayHello *(3)" " + " " + x)

# # data types:
# basicDataTypes(int, float, double, complex, bool, str)
# list[], set{}, frozenset({}), tuple(), dict{value:key}, range(n)

# for x in sayHello:
#     print(len(sayHello))


while True:
    plate = input("Enter a new plate")
    plate = plate.upper()
    if len(plate) == 0:
        break
    if len(plate) == 5: 
        res = "Bike"
    elif len(plate) == 6 and plate [:5] >= "A" and plate [:5] <= "Z":
        res = "Bike"
    else:
        res = "Car"
    print("The vehicle is: " + res)
