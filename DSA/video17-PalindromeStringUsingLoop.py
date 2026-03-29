# s = "nikhil"
s = "mom"
l = 0
r = len(s) - 1

flag = True
while l <= r:
    if s[l] == s[r]:
        l += 1
        r -= 1
    else:
        flag = False
        break
print(flag)