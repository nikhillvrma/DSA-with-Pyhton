arr = [8, 9, 6, 4, 7, 10, 3, 5, 2, 1]
for i in range(len(arr)):
    max_val = i
    for j in range(i+1, len(arr)):
        if arr[j] > arr[max_val]:
            max_val = j
    arr[i], arr[max_val] = arr[max_val], arr[i]
print(arr)    