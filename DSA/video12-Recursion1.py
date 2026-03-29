# Print 10 times "I Proud to be a Sanatani Hindu" using recursion

count = 0
def statement():
    print("I Proud to be a Sanatani Hindu")
    global count
    count += 1
    if count == 10:
        return
    statement()
    
r = statement()
print(r)