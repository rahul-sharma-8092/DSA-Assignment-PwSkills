# <<----function definition---->>
def arrange_coins(n):
    complete_rows = 0
    row_coins = 1

    while n >= row_coins:
        complete_rows += 1
        n -= row_coins
        row_coins += 1

    return complete_rows


# <<----function calling---->>
n = 5

result = arrange_coins(n)
print(result)
