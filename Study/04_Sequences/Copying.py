cars = ["Toyota","Lexus","Acura","Honda","Infinity","GM"]

copy_cars = cars.copy()

cars.remove("GM")
copy_cars.append("Subaru")

print(id(cars), cars)
print(id(copy_cars), copy_cars)