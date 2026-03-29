# Print the Number 1 to N and the value of N will be given by the user
count = 0
def printNum(n):
    global count
    if count == n:
        return
    print(count+1)
    count += 1
    printNum(n)

n = int(input("Enter the Nth Number to print 1 to N : "))
printNum(n)
