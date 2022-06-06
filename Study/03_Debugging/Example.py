# a function to square a number
def get_square(n):
    square_number = n*n
    return square_number

start_number = 1
stop_number = 10

for i in range(start_number,stop_number + 1):
    square_number = get_square(i)
    print("Square number of {0:3} is {1:3}".format(i, square_number))
