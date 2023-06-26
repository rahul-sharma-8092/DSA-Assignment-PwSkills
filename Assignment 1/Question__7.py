# <<----function definition---->>
def moveZeroes(nums):
    left = 0
    for right in range(len(nums)):
        if nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
    while left < len(nums):
        nums[left] = 0
        left += 1


# <<----function Calling---->>
nums = [0, 1, 0, 3, 12]
moveZeroes(nums)
print(nums)
