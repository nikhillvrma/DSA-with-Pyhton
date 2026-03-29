def palindromeNumber(num):
    n = num
    result = 0
    while n > 0:
        rem = n % 10
        result = (result * 10) + rem
        n = n // 10
    if result == num:
        return True
    else:
        return False


num = int(input("Enter a Number: "))
r = palindromeNumber(num)
print(r)
