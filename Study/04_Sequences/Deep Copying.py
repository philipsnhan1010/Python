cars = [
    ["Raw4","Lap"],
    ["CRV"],"Luong Nhan",
    ["Crosstrek","Myan"]
]

# Basic copying
# copy_cars = cars.copy()
# cars[1][0] = "Camry"
# print(id(cars), cars)
# print(id(copy_cars), copy_cars)

# Deep Copying
import copy
c_cars = copy.deepcopy(cars)
cars[1][0] = "Corrola"
print(id(cars), cars)
print(id(c_cars), c_cars)