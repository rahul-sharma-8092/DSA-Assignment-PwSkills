# <<----function definition---->>
def findMissingRanges(nums, lower, upper):
    result = []
    start = lower

    for num in nums + [upper + 1]:
        if num > start:
            if num - 1 == start:
                result.append(str(start))
            else:
                result.append(str(start) + "," + str(num - 1))
        start = num + 1

    return result


# <<----function calling---->>
nums = [0, 1, 3, 50, 75]
lower = 0
upper = 99
print(findMissingRanges(nums, lower, upper))
