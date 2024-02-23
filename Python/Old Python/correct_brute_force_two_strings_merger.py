def merge(word1: str, word2: str) -> str:
    word: str = "" 
    if len(word1) < len(word2):
        for i in range(len(word2) - len(word1)):
            word1 += " "
    else:
        for i in range(len(word1) - len(word2)):
            word2 += " "
    for i in range(len(word1)):
        if word1[i] != " ":
            word += word1[i]
        if word2[i] != " ":
            word += word2[i]
    return word


def main():
    print(merge("ab", "pqrs"))
    return 0


if __name__ == "__main__":
    main()
