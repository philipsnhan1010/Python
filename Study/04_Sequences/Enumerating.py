cars = "Toyota,Lexus,Acura,Honda,Infinity,GM"

# Split list
cars_list = cars.split(",")
print(cars_list)

# Which brand is Lexus
print(cars_list.index("Lexus"))

# Print brand with number
for brand_num, brand_name in enumerate(cars_list):
    print("Brand number {0} is {1}".format(brand_num + 1, brand_name))