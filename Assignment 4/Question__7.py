# <<----function definition---->>
def max_count(m, n, ops):
    min_row = m
    min_col = n

    for op in ops:
        min_row = min(min_row, op[0])
        min_col = min(min_col, op[1])

    return min_row * min_col


# <<----function calling---->>
m = 3
n = 3
ops = [[2, 2], [3, 3]]

result = max_count(m, n, ops)
print(result)
