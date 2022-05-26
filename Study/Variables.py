##Variables
#---------------------------------------------------------------------------------
x = 5
print(x)
print(type(x))

y = "Lap"
y1 = 'Thu'
print(y)
print(type(y))
print(y1)

z = float(9)
print(z)
print(type(z))

#---------------------------------------------------------------------------------
##Variable Names
#---------------------------------------------------------------------------------
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

#Camel Case
myVariableName = "Lap"
#Pascal Case
MyVariableName = "Lap"
#Snake Case
my_variable_name = "Lap"

#---------------------------------------------------------------------------------
##Variable Assign Multiple Values
#---------------------------------------------------------------------------------
x, y, z = "Sunny", "Rainny", "Windy"
print(x)
print(y)
print(z)

a = b = c = 10
print(a)
print(b)
print(c)

#Unpack a Collection
fruits = ["Apple", "Orange", "Pinepaple"]
x, y, z = fruits
print(x)
print(y)
print(z)

#---------------------------------------------------------------------------------
##Output Variables
#---------------------------------------------------------------------------------
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)
print(x + y + z)

x = 5
y = "Lap"
print(x, y)

#---------------------------------------------------------------------------------
##Global Variables
#---------------------------------------------------------------------------------
x = "Sunny"

def myFunc():
    global x #keyword global use to create a global variable
    x = "Rainny"
    print("1: Today is " + x)
myFunc()
print("2: Today is " + x)
