# def sumValues(sum, i, n):
#     if i > n:
#         print(sum)
#         return
#     sumValues(sum+i, i+1, n)
    
# sum = 0
# i = int(input("Enter the First Number from where you want to start adding values : "))
# n = int(input("Enter the Last the Number where you want to stop : "))
# sumValues(sum, i, n)


def func(n):
    if n == 1:
        return 1
    return n + func(n-1)

n = int(input("Enter the Last Digit : "))
r = func(n)
print(r)