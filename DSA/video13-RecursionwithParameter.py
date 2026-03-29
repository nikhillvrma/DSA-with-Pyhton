# Print 1 to N using Tail Recursion


def tailRecursion(i, n):
    if i > n:
        return
    print(i)
    tailRecursion(i + 1, n)

n = int(input("Enter the Nth Value : "))
tailRecursion(1, n)