def quick_sort(nums, low, high):
    if low < high:
        p = partition(nums, low, high)
        quick_sort(nums, low, p - 1)
        quick_sort(nums, p + 1, high)
    return nums


def partition(nums, low, high):
    pivot = nums[low]
    i = low
    j = high
    while i < j:
        while i <= high and nums[i] <= pivot:
            i += 1
        while j >= low and nums[j] > pivot:
            j -= 1
        if i < j:
            nums[i], nums[j] = nums[j], nums[i]
            
    nums[low], nums[j] = nums[j], nums[low]
    return j


nums = [4, 1, 3, 2, 8, 6, 7]
low = 0
high = len(nums) - 1
print("Array is : ", nums)
result = quick_sort(nums, low, high)
print("Sorted Array is : ", nums)
