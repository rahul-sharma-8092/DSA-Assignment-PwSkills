# <<----function definition---->>
def search(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1


# <<----function Calling---->>
nums = [-1, 0, 3, 5, 9, 12]
target = 9
result = search(nums, target)
print(result)
