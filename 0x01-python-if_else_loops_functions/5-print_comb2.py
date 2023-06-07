#!/usr/bin/python3
for j in range(0, 100):
    if j == 99:
        print("{j}".format(j=j))
    else:
        print("{j:02}".format(j=j), end=", ")
