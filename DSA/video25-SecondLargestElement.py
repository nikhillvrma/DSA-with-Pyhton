def secondLargestElement(nums):

    # Method 1:
    largest = float("-inf")
    secondlargest = float("-inf")
    n = len(nums)
    if not nums:
        return None

    for i in range(n):
        largest = max(largest, nums[i])

    for i in range(n):
        if nums[i] > secondlargest and nums[i] < largest:
            secondlargest = nums[i]
    return secondlargest

    # Method 2:
    largest = float("-inf")
    secondlargest = float("-inf")
    n = len(nums)
    for i in range(n):
        if nums[i] > largest:
            secondlargest = largest
            largest = nums[i]
        if nums[i] > secondlargest and nums[i] < largest:
            secondlargest = nums[i]
            
    return secondlargest


nums = [55, 32, 97, -55, 45, 32, 88, 21]
result = secondLargestElement(nums)
print(result)
