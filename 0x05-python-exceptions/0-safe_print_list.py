#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        j = 0
        k = 0
        for i in my_list:
            j = j + 1
        for i in range(x):
            print("{}".format(my_list[i]), end="")
            k = k + 1
    except x > j:
        pass
    finally:
        print()
        return k
