# <<----function definition---->>
def isMonotonic(nums):
    isIncreasing = True
    isDecreasing = True

    for i in range(1, len(nums)):
        if nums[i] < nums[i-1]:
            isIncreasing = False
        if nums[i] > nums[i-1]:
            isDecreasing = False
    return isIncreasing or isDecreasing


# <<----function Calling---->>
nums = [1, 2, 2, 3]
result = isMonotonic(nums)
print(result)
