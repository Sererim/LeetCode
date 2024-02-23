'''Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]'''


def productExceptSelf(nums: list[int]) -> list[int]:

    nums_dict = {i: x for i, x in enumerate(nums)}
    print(nums_dict.items())
    temp = [1 for _ in range(len(nums))]
    val: int = 0
    
    for i in nums_dict.keys():
        val, nums_dict[i] = nums_dict.get(i), 1
        for x in nums_dict.values():
            temp[i] *= x
        nums_dict[i] = val
 
    print(temp)
    return temp

if __name__ == "__main__":
    print(productExceptSelf([1,2,3,4])) if productExceptSelf([0,0]) == [0,0] else None
