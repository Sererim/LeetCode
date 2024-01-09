# Example 1:
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7].
# In this case, the max area of water (blue section) the container can contain is 49.
#
# Example 2:
#
# Input: height = [1,1]
# Output: 1
from typing import List


# BRUTE FORCE METHOD
def max_area(height: List[int]) -> int:
    result: int = 0
    area: int = 0

    if len(height) > 2:
        for left in range(len(height)):
            for right in range(len(height) - 1, left, -1):
                area = (right - left) * min(height[left], height[right])
                result = max(area, result)
    else:
        result = min(height[0], height[-1])
    return result


# SMART METHOD
def smart_max_area(height: List[int]) -> int:
    result: int = 0
    left, right = 0, len(height) - 1

    while left < right:
        area = (right - left) * min(height[left], height[right])
        result = max(area, result)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return result


if __name__ == '__main__':
    assert max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    assert max_area([1, 1]) == 1
