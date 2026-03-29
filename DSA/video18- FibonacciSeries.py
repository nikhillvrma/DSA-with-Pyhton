count = 0
def fib(a, b, num):
    global count
    if count-1 < num:
        print(a, end=", ")
        next_Value = a + b
        a = b
        b = next_Value
        count += 1
        fib(a, b, num)

num = int(input("Enter the last Number : "))
sum = 0
n = 1
fib(sum, n, num)