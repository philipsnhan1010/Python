highest_number = 100

for test_prime in range(2,highest_number + 1):
    if test_prime == 2:
        print("{0} is prime a number".format(test_prime))
        continue
    if_prime = True
    for possible_prime in range(2,test_prime):
        if test_prime % possible_prime == 0:
            if_prime = False
    if if_prime:
        print("{0} is prime a number".format(test_prime))

print("Completed!")