# <<----function definition---->>
def find_missing_elements(nums1, nums2):
    set1 = set(nums1)
    set2 = set(nums2)

    answer1 = [num for num in nums1 if num not in set2]
    answer2 = [num for num in nums2 if num not in set1]

    return [answer1, answer2]


# <<----function calling---->>
nums1 = [1, 2, 3]
nums2 = [2, 4, 6]

result = find_missing_elements(nums1, nums2)
print(result)
