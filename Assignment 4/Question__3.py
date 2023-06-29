# <<----function definition---->>
def transpose(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    transpose = []
    for j in range(cols):
        row = []
        for i in range(rows):
            row.append(matrix[i][j])
        transpose.append(row)

    return transpose


# <<----function calling---->>
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

result = transpose(matrix)
print(result)
