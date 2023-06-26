from collections import Counter

# <<----function definition---->>


def findLHS(nums):
    num_freq = Counter(nums)
    max_length = 0

    for num in num_freq:
        if num + 1 in num_freq:
            curr_length = num_freq[num] + num_freq[num + 1]
            if curr_length > max_length:
                max_length = curr_length
    return max_length


# <<----function Calling---->>
nums = [1, 3, 2, 2, 5, 2, 3, 7]
result = findLHS(nums)
print(result)
