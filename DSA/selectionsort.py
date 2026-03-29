arr = [8,9,6,4,7,10,3,5,2,1]
for i in range(len(arr)):
    temp = i
    for j in range(i+1, len(arr)):
        if arr[j] < arr[temp]:
            temp = j
    arr[i], arr[temp] = arr[temp], arr[i]
print(arr)