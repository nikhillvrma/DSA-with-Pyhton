def merge_sort(arr):
    if len(arr)<=1:
        return arr
    mid = len(arr)//2
    left_arr = arr[:mid]
    right_arr = arr[mid:]
    left = merge_sort(left_arr)
    right = merge_sort(right_arr)
    return merge_arr(left, right)

def merge_arr(left, right):
    i, j = 0, 0
    n, m = len(left), len(right)
    result = []
    while i<n and j<m:
        if left[i] <= right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
            
    if i<n:
        while i<n:
            result.append(left[i])
            i+=1
    elif j<m:
        while j<m:
            result.append(right[j])
            j+=1
            
# we can write these lines instead of the lines 23 to 28
    # result.extend(left[i:])
    # result.extend(right[j:])
# These two lines of the code also adds the extra remaining elements from the left sorted arrays
    return result


arr = [3, 2, 5, 1, 9, 6, 7 ,1, 3, 7, 4]
sorted_arr = merge_sort(arr)
print("Array is : ", arr)
print("Sorted Array is : ", sorted_arr)