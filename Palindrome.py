class Solution:
    def isPalindrome(self, x: int) -> bool:
        pal = str(x)
        return pal == pal[::-1]


def main():
    pal: object = Solution()
    i: int = -100
    print(pal.isPalindrome(i))

if __name__ == "__main__":
    main()
