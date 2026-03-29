# arr = [9, 2, 8, 6, 4, 7, 10, 3, 5, 1]
arr = [2, 4, 5, 6, 7, 8, 9, 10, 12, 14, 16]
for i in range(len(arr) - 2, -1, -1):
    is_swap = False
    for j in range(0, i + 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            is_swap = True
    if is_swap==False:
        break
print(arr)