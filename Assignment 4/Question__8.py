# <<----function definition---->>
def shuffle(nums, n):
    i = 0
    j = n
    result = []
    while i < n:
        result.append(nums[i])
        result.append(nums[j])
        i += 1
        j += 1

    return result


# <<----function calling---->>
nums = [2, 5, 1, 3, 4, 7]
n = 3
result = shuffle(nums, n)
print(result)
