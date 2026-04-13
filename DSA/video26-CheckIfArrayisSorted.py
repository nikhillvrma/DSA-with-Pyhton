def checking(nums):
    if len(nums) == 0:
        return None
    if len(nums) == 1:
        return True
    for i in range(len(nums)-1):
        if nums[i] > nums[i+1]:
            return False
    return True

nums = [2, 4, 6, 8, 10, 12, 14]
result = checking(nums)
print(result)