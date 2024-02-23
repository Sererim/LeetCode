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
    i, j = 0, len(s) - 1
    ls_s: list[str] = list(s)
    
    while i < j:
        if ls_s[i] in vowels:
            if ls_s[j] in vowels:
                ls_s[i], ls_s[j] = ls_s[j], ls_s[i]
                i += 1
                j -= 1
            else:
                j -= 1
        else:
            i += 1 
    
    return "".join(ls_s)


if __name__ == "__main__":
    if reverseVowels("leetcode") == "leotcede":
        print("YES")
