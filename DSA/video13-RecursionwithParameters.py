# Print whatever the user wants and also ask to the user that how many times to print

def userChoice(x, n):
    if n==0:
        print("Task has been Completed!!!")
        return
    print(x)
    userChoice(x, n-1)

x = input("Tell us what you want to print : ")
n = int(input("Tell us how many time you want to print : "))
userChoice(x, n)