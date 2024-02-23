# For two strings s and t, we say "t divides s" if and only if s = t + ... + t (i.e., t is concatenated with itself one or more times).

# Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.


# Example 1:

# Input: str1 = "ABCABC", str2 = "ABC"
# Output: "ABC"
# Example 2:

# Input: str1 = "ABABAB", str2 = "ABAB"
# Output: "AB"
# Example 3:

# Input: str1 = "LEET", str2 = "CODE"
# Output: ""
from math import gcd


def gcd_of_strings(str1: str, str2: str) -> str:
    div: int = gcd(len(str1), len(str2))
    out: str = ""

    
    
    if len(set(str1)) == len(set(str2)):
        if str1[:div] == str2[:div] and str1[len(str1) - div:] == str2[len(str2) - div:]:
            out = str2[:div]

    return out


if __name__ == "__main__":
    print(gcd_of_strings("ABABCCABAB", "ABAB"))
