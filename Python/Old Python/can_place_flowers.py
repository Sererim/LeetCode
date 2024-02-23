# You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

# Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

# Example 1:

# Input: flowerbed = [1,0,0,0,1], n = 1
# Output: true

# Example 2:
# Input: flowerbed = [1,0,0,0,1], n = 2
# Output: false

def canPlaceFlowers(flowerbed: list[int], n: int) -> bool:
    to_place: int = n
    result: bool = True
    length = len(flowerbed)
    
    # We will check the flowerbed for a suitable conditions middle and both ends will be checked
    for i in range(length):
        if i != 0 and i + 1 != length:
            # If flowerbed to the right and left are empty and flowerbed at i is empty
            # we will put there a flower and count down to_place variable
            if flowerbed[i - 1] == 0 and flowerbed[i] == 0 and flowerbed[i + 1] == 0:
                flowerbed[i] = 1
                to_place -= 1
        elif i == 0 and i + 1 != length:
            if flowerbed[i] == 0 and flowerbed[i + 1] == 0:
                flowerbed[i] = 1
                to_place -= 1
        elif i + 1 == length:
            if flowerbed[i - 1] == 0 and flowerbed[i] == 0:
                flowerbed[i] = 1
                to_place -= 1
    
    # If to_place == 0 then it means that all flowers were put into the flowerbed
    result = True if to_place == 0 or to_place < 0 else False

    return result


if __name__ == "__main__":
    print(canPlaceFlowers([0,0,1,0,0], 1))
