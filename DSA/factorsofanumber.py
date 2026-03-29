from math import *


def allFactors(num):
    n = num
    lst = []
    # for i in range(1, n+1//2):
    #     if num%i == 0:
    #         lst.append(i)
    # lst.append(num)
    # return lst

    # method 2
    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0:
            lst.append(i)
            if n // i != i:
                lst.append(n // i)

    return sorted(lst)

num = int(input("Enter a Number: "))
r = allFactors(num)
print(r)
