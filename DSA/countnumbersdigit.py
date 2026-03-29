def countNumbers(num):
    n = num
    counts = 0
    while n > 0:
        n //= 10
        counts += 1
    return counts


num = int(input("Enter a Number: "))
r = countNumbers(num)
print(r)
