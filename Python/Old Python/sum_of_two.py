class Solution:
    def two_sum(self, nums: list[int], target: int) -> list[int]:
        d = {}
        for index, num in enumerate(nums):
            if target - num in d:
                return [d[target - num], index]
            else:
                d[num] = index


def main():
    two: Solution = Solution()
    print(two.two_sum([2, 7, 11, 15], 9))
    return


if __name__ == "__main__":
    main()
