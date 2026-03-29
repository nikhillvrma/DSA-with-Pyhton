def armstrongNumber(num):
    if num < 0:
        return False

    n = m = num
    result = 0
    c = 0
    while n > 0:
        n //= 10
        c += 1
    while m > 0:
        rem = m % 10
        result = result + (rem**c)
        m //= 10
    if result == num:
        return True
    else:
        return False


num = int(input("Enter a number: "))
r = armstrongNumber(num)
print(r)
