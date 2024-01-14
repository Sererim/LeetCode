# Example 1:
#
# Input: arr = [1,2,2,1,1,3]
# Output: true
# Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
# Example 2:
#
# Input: arr = [1,2]
# Output: false
# Example 3:
#
# Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
# Output: true

from typing import List

# Slow and heavy because of creating a dict and a set.


def unique_occurrences(arr: List[int]) -> bool:
    d = {num: arr.count(num) for num in arr}
    return True if len(set(d.values())) == len(d.values()) else False


if __name__ == '__main__':
    assert unique_occurrences([1, 2, 2, 1, 1, 3])
    assert not unique_occurrences([1, 2])
    assert unique_occurrences([-3, 0, 1, -3, 1, 1, 1, -3, 10, 0])
