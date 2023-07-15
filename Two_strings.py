def merge(word1: str, word2: str) -> str:
    d_word: str = word1 + word2[::-1]
    word: str = ""
    if len(d_word) % 2 == 0:
        for i in range(int(len(d_word) / 2)):
            word += d_word[i] + d_word[len(d_word) - i - 1]
    else:
        for i in range(int(len(d_word) / 2)):
            word += d_word[i] + d_word[len(d_word) - i - 1]
        word += d_word[int(len(d_word) / 2)]    
    return word


def main():
    print(merge("ab", "pqrs"))
    return 0


if __name__ == "__main__":
    main()
