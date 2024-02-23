# Example 1:
#
# Input: nums = [1,7,3,6,5,6]
# Output: 3
# Explanation:
# The pivot index is 3.
# Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
# Right sum = nums[4] + nums[5] = 5 + 6 = 11
#
# Example 2:
#
# Input: nums = [1,2,3]
# Output: -1
# Explanation:
# There is no index that satisfies the conditions in the problem statement.
#
# Example 3:
#
# Input: nums = [2,1,-1]
# Output: 0
# Explanation:
# The pivot index is 0.
# Left sum = 0 (no elements to the left of index 0)
# Right sum = nums[1] + nums[2] = 1 + -1 = 0

from typing import List


def pivot_index(nums: List[int]) -> int:
    left_sum: int = 0
    right_sum: int = sum(nums[1:])
    answer: int = -1

    for i, _ in enumerate(nums):
        if left_sum == right_sum:
            answer = i
            break
        elif i + 1 < len(nums):
            left_sum += nums[i]
            right_sum -= nums[i + 1]

    return answer


if __name__ == '__main__':
    assert pivot_index([1, 7, 3, 6, 5, 6]) == 3
    assert pivot_index([1, 2, 3]) == -1
    assert pivot_index([2, 1, -1]) == 0
