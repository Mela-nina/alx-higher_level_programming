#!/usr/bin/python3
for j in range(97, 123):
    if f"{j:c}" != "q" and f"{j:c}" != "e":
        print("{j:c}".format(j=j), end="")
