def arrayReverse(left, right, arr):
    if left > right and right < left:
        print(arr)
        return
    
    temp = arr[left]
    arr[left] = arr[right]
    arr[right] = temp
    arrayReverse(left+1, right-1, arr)

arr = [5, 7, 3, 2, 6, 1, 5, 9]
left = int(input("Enter the starting index : "))
right = int(input("Enter the ending index : "))
arrayReverse(left, right, arr)