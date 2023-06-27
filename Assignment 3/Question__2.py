# <<----function definition---->>
def fourSum(nums, target):
    nums.sort()
    result = []
    findQuadruplets(nums, target, 4, [], result)
    return result


def findQuadruplets(nums, target, k, currentQuadruplet, result):
    if k == 2:
        left, right = 0, len(nums) - 1
        while left < right:
            currentSum = nums[left] + nums[right]
            if currentSum == target:
                result.append(currentQuadruplet + [nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif currentSum < target:
                left += 1
            else:
                right -= 1
    else:
        for i in range(len(nums) - k + 1):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            findQuadruplets(
                nums[i + 1:],
                target - nums[i],
                k - 1,
                currentQuadruplet + [nums[i]],
                result,
            )


# <<----function calling---->>
nums = [1, 0, -1, 0, -2, 2]
target = 0
print(fourSum(nums, target))
