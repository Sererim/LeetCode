# Given a string s, reverse only all the vowels in the string and return it.

# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

# Example 1:

# Input: s = "hello"
# Output: "holle"
# Example 2:

# Input: s = "leetcode"
# Output: "leotcede"

# BAD 

def reverseVowels( s: str) -> str:
    vowels: list[str] = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    length: int = len(s)
    in_s: list[str] = []
    ls_s: list[str] = [i for i in s]
    
    for _, x in enumerate(s):
        if x in vowels:
            in_s.append(x)
    
    for i in range(length):
        if ls_s[i] in vowels:
            ls_s[i] = in_s[-1]
            in_s.pop(-1)
    
    s = ""
    return s.join(ls_s)


if __name__ == "__main__":
    if reverseVowels("hello") == "holle":
        print("YES")
