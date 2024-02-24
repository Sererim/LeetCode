def mergeAlternately( word1: str, word2: str) -> str:
    result: str = ""
    
    if len(word1) < len(word2):
        word1 += " " * (len(word2) - len(word1))
    if len(word1) > len(word2):
        word2 += " " * (len(word1) - len(word2))
    
    for i, letter in enumerate(word1):
        result += letter
        result += word2[i]
        
    print(result.replace(" ", ""))
    return result.replace(" ", "")


if __name__ == '__main__':
    assert mergeAlternately(word1="abcd", word2="pq") == "apbqcd"

# Runtime 43 ms Beats 17.61%
# 16.51 MB Beats 74.11%
