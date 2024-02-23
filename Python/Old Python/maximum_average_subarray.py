# Example 1:
#
# Input: nums = [1,12,-5,-6,50,3], k = 4
# Output: 12.75000
# Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
#
# Example 2:
#
# Input: nums = [5], k = 1
# Output: 5.00000
from typing import List


# Works fine for most testcases, except for retarded one, that soymen at leetcode addede just for fun.
# Python isn't a language of choice to process list of len > 100
# Okay
def find_max_average_slow(nums: List[int], k: int) -> float:
    index: int = 0
    temp: float = 0
    answer: float = float('-inf')

    if len(nums) == k:
        answer = sum(nums) / len(nums)
    else:
        while index + k < len(nums) + 1:
            temp = sum(nums[index: index + k]) / k
            if answer < temp:
                answer = temp
            index += 1
    print(answer)
    return answer


# BIG BRAIN
def find_max_average(nums: List[int], k: int) -> float:
    answer: float = sum(nums[:k])
    temp: float = answer
    index: int = k
    prefix: int = 0

    while index < len(nums):
        temp += nums[index]
        temp -= nums[prefix]
        if answer < temp:
            answer = temp
        index += 1
        prefix += 1

    return answer / k


if __name__ == '__main__':
    assert find_max_average([1, 12, -5, -6, 50, 3], 4) == 12.75
    assert find_max_average([5], 1) == 5.0000
    assert find_max_average([0, 1, 1, 3, 3], 4) == 2.000
