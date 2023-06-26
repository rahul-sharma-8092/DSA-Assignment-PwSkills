# <<----function definition---->>
def maxCandies(candyType):
    unique_count = len(set(candyType))
    max_candies = min(unique_count, len(candyType) // 2)
    return max_candies


# <<----function Calling---->>
candyType = [1, 1, 2, 2, 3, 3]
result = maxCandies(candyType)
print(result)
