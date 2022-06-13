# Create a list
from numpy import insert


brand = []

# Add a couple of brand name
brand.insert(0,"Toyota")
brand.insert(0,"Lexus")

# Add item by Append: Append will add item at the end of list
brand.append("Honda")

# Add a list to a list
brand_name = ["Acura","Infinity"]

#brand = brand.__add__(brand_name)
#brand.append(brand_name)
brand.extend(brand_name)

# Remove an item
brand.remove("Infinity")

# Pop an item: Remove an item from a list and also get the access to that item
my_car = brand.pop(1)
print(my_car)

# Clear the list
brand.clear()

print(brand)