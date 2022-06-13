import sys

paths = sys.path

for p in paths:
    print(p)
    print(p.partition("\\"))
    print(p.rpartition("\\"))

    print(p.split("\\")[-1])
    print(p.rpartition("\\")[-1])

