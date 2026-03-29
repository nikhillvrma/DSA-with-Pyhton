def factorial(n):
    if n == 1:
        return 1
    return n*factorial(n-1)

n = int(input("Enter the number whose factorial you want to calculate : "))
r = factorial(n)
print(r)