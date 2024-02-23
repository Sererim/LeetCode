def removeElement(nums: list[int], val: int) -> int:
    box: int = 0
    for i in range(len(nums)):
        if nums[i] == val:
            box = nums[i]
            for j in range()


def main():
    l: list[int] = [3,2,2,3]
    val: int = 2
    print(removeElement(l, 3))


if __name__ == "__main__":
    main()
