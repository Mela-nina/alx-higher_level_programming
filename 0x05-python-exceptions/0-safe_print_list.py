#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    ret = 0
    for j in range(x):
        try:
            print(f"{my_list[j]}", end="")
            ret += 1
        except IndexError:
            break
    print()
    return (ret)
