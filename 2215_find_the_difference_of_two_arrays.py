# Example 1:
#
# Input: nums1 = [1,2,3], nums2 = [2,4,6]
# Output: [[1,3],[4,6]]
# Explanation:
# For nums1, nums1[1] = 2 is present at index 0 of nums2, whereas nums1[0] = 1 and nums1[2] = 3 are not present in nums2. Therefore, answer[0] = [1,3].
# For nums2, nums2[0] = 2 is present at index 1 of nums1, whereas nums2[1] = 4 and nums2[2] = 6 are not present in nums2. Therefore, answer[1] = [4,6].
# Example 2:
#
# Input: nums1 = [1,2,3,3], nums2 = [1,1,2,2]
# Output: [[3],[]]
# Explanation:
# For nums1, nums1[2] and nums1[3] are not present in nums2. Since nums1[2] == nums1[3], their value is only included once and answer[0] = [3].
# Every integer in nums2 is present in nums1. Therefore, answer[1] = [].

from typing import  List


def find_difference(nums1: List[int], nums2: List[int]) -> List[List[int]]:
    return [list(set(nums1) - set(nums2)), list(set(nums2) - set(nums1))]


if __name__ == '__main__':
    assert find_difference([1, 2, 3], [2, 4, 6]) == [[1, 3], [4, 6]]
    assert find_difference([1, 2, 3, 3], [1, 1, 2, 2]) == [[3], []]
