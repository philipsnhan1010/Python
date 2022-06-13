cars = "Toyota, Lexus, Acura, Honda, Infinity, GM"

# Split list
cars_list = cars.split(",")
print(cars_list)

# Join list back
rejoined_list = " | ".join(cars_list[-1::-1])
print(rejoined_list)