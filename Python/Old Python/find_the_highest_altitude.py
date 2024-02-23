# Example 1:
#
# Input: gain = [-5,1,5,0,-7]
# Output: 1
# Explanation: The altitudes are [0,-5,-4,1,1,-6]. The highest is 1.
# Example 2:
#
# Input: gain = [-4,-3,-2,-1,4,3,2]
# Output: 0
# Explanation: The altitudes are [0,-4,-7,-9,-10,-6,-3,-1]. The highest is 0.

from typing import List

# gain[i]=altitude[i+1]-altitude[i]


def largest_altitude(gain: List[int]) -> int:
    altitudes: List[int] = [0]

    for _, num in enumerate(gain):
        altitudes.append(num + altitudes[-1])
    # print(max(altitudes))
    return max(altitudes)


if __name__ == '__main__':
    assert largest_altitude([-5, 1, 5, 0, -7]) == 1
    assert largest_altitude([-4, -3, -2, -1, 4, 3, 2]) == 0
