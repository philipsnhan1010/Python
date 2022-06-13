useful_info = (
    # Lithuanian long-jumping record holder
    ["Povilas Mykolaitis","Long jump",2011],
    # baked beans in 3 mins with cocktail stick
    159,
    # Lap cars
    ("Rav4","RX350")
)

# List out all item
for item in useful_info:
    print(item,type(item))

# Unpacking tulpe
povilas, baked_bean, cars = useful_info
print(povilas)
print(baked_bean)
print(cars)
