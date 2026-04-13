def largestElement(arr):
    if len(arr) == 0:
        return None  # Return None for an empty array

    largest = arr[0]  # Initialize largest with the first element

    for num in arr:
        largest = max(largest, arr[num])

    return largest

arr=[4, ]
