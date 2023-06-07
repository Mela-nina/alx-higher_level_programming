#!/usr/bin/python3
for j in range(0, 10):
    for k in range(1 + j, 10):
        if j == 8:
            print("{}{}".format(j, k))
        else:
            print("{}{}".format(j, k), end=", ")
