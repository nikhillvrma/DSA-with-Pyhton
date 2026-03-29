arr = [9, 2, 8, 6, 4, 7, 10, 3, 5, 1]
for i in range(1, len(arr)):
    j=i-1
    key = arr[i]
    while j>=0 and arr[j]>key:
        arr[j+1] = arr[j]
        j-=1
    arr[j+1] = key
print(arr)