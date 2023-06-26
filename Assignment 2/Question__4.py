# <<----function definition---->>
def canPlaceFlowers(flowerbed, n):
    count = 0
    length = len(flowerbed)
    for i in range(length):
        if flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] == 0) and (i == length-1 or flowerbed[i+1] == 0):
            flowerbed[i] = 1
            count += 1
    return count >= n


# <<----function Calling---->>
flowerbed = [1, 0, 0, 0, 1]
n = 1
result = canPlaceFlowers(flowerbed, n)
print(result)
