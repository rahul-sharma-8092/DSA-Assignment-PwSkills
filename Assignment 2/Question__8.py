# <<----function definition---->>
def minimumScore(nums, k):
    overall_min = min(nums)
    overall_max = max(nums)
    initial_score = overall_max - overall_min

    if initial_score <= 2 * k:
        return initial_score

    new_min = max(overall_min - k, min(nums) + k)
    new_max = min(overall_max + k, max(nums) - k)
    new_score = new_max - new_min
    return new_score


# <<----function Calling---->>
nums = [1]
k = 0
result = minimumScore(nums, k)
print(result)
