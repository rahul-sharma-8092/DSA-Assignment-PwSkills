# <<----function definition---->>
def findErrorNums(nums):
    i = 0
    n = len(nums)
    while i < n:
        if nums[i] != i + 1 and nums[nums[i] - 1] != nums[i]:
            nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        else:
            i += 1
    for i in range(n):
        if nums[i] != i + 1:
            return [nums[i], i + 1]


# <<----function Calling---->>
nums = [1, 2, 2, 4]
result = findErrorNums(nums)
print(result)
