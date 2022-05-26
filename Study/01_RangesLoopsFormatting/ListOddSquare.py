## While
i = 1
while i <= 100:
    square = i*i
    # print("The square of " + str(i) + " is " + str(square))
    print("The square of {0} is {1}".format(str(i), str(square)))
    i+=2
else:
    print("Never executes")
print("Complete")