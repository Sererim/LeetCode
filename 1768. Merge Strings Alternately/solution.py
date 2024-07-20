import re
from functools import reduce


def mergeAlternately(word1: str, word2: str) -> str:
    word1 = (
        word1 + ((len(word2) - len(word1)) * " ") if len(word1) < len(word2) else word1
    )
    word2 = (
        word2 + ((len(word1) - len(word2)) * " ") if len(word2) < len(word1) else word2
    )
    word = list(zip(word1, word2))

    return re.sub(" ", "", reduce(lambda acc, tpl: acc + "".join(tpl), word, ""))


if __name__ == "__main__":
    print(mergeAlternately("abc", "pqr"))
