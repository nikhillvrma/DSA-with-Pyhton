arr = [9, 2, 8, 6, 4, 7, 10, 3, 5, 1]
for i in range(len(arr)-2, -1, -1):
    for j in range(0, i+1):
        if arr[j]>arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
print(arr)