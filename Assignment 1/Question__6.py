# <<----function definition---->>
def containsDuplicate(nums):
    seen = set()

    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False


# <<----function Calling---->>
nums = [1, 2, 3, 1]
result = containsDuplicate(nums)
print(result)  # Output: True
