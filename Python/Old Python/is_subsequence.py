"""
Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false
"""


def is_subsequence(s: str, t: str) -> bool:
    answer = list(filter(lambda n: n in [*s] and n in [*t], t))
    print(answer)
    print([*s])
    return True if answer == [*s] else False


def correct_subsequence(s: str, t: str) -> bool:
    i, j = 0, 0  # Pointers for tracking characters in s and t respectively

    # Loop until we reach the end of either s or t
    while i < len(s) and j < len(t):
        # If the current character in s matches the current character in t
        if s[i] == t[j]:
            i += 1  # Move pointer in s to the next character
        j += 1  # Move pointer in t to the next character

    # If we have reached the end of s, it means all characters in s were found in t
    return i == len(s)


if __name__ == '__main__':
    assert is_subsequence(s="abc", t="ahbgdc")
    assert not is_subsequence(s="axc", t="ahbgdc")
    assert is_subsequence(s="ab", t="baab")
