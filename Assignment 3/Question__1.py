# <<----function definition---->>
def threeSumClosest(nums, target):
    nums.sort()
    n = len(nums)
    closestSum = float('inf')

    for i in range(n - 2):
        left = i + 1
        right = n - 1
        while left < right:
            currentSum = nums[i] + nums[left] + nums[right]
            if abs(currentSum - target) < abs(closestSum - target):
                closestSum = currentSum
            if currentSum > target:
                right -= 1
            elif currentSum < target:
                left += 1
            else:
                return target
    return closestSum


# <<----function calling---->>
nums = [-1, 2, 1, -4]
target = 1
print(threeSumClosest(nums, target))
