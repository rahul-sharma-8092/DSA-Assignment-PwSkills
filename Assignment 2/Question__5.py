# <<----function definition---->>
def maximumProduct(nums):
    nums.sort()
    max_product = nums[-1] * nums[-2] * nums[-3]
    alt_product = nums[0] * nums[1] * nums[-1]
    return max(max_product, alt_product)


# <<----function Calling---->>
nums = [1, 2, 3]
result = maximumProduct(nums)
print(result)
