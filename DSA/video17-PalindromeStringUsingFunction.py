def palindrome(str, l, r):
    if l >= r:
        return True     
    if str[l] != str[r]:
        return False
    return palindrome(str, l+1, r-1)
    
str = input("Enter the String : ")
l = 0
r = len(str)-1
result = palindrome(str, l, r)
print(result)