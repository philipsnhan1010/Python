i = 0
while True:
    i += 1
    if i > 100:
        break
    if i % 3 != 0:
        continue
    print(i,"Fizz")

print("Completed")