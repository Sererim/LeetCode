"""
Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
"""
from typing import List


def move_zeroes(nums: List[int]) -> List[int]:
    length: int = len(nums)
    nums = list(filter(lambda n: n != 0, nums))
    nums += [0] * (length - len(nums))
    print(nums)
    return nums


if __name__ == '__main__':
    assert move_zeroes([0, 1, 0, 3, 12]) == [1, 3, 12, 0, 0]
    assert move_zeroes([0]) == [0]
    assert move_zeroes([0, 0, 1]) == [1, 0, 0]
