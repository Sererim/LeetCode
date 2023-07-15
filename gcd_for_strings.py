def gcd(str1: str, str2: str) -> str:
    out: str = ""

    if len(str1) > len(str2):
        for i in range(len(str2)):
            if str1[i] == str2[i]:
                out += str2[i]
            else:
                break
    elif len(str2) > len(str1):
        for i in range(len(str1)):
            if str1[i] == str2[i]:
                out += str1[i]
            else:
                break
    else:
        for i in range(len(str1)):
            if str1[i] == str2[i]:
                out += str1[i]
            else:
                break
    return out


def main():
    print(gcd("ABABAB", "ABAB"))
    return


if __name__ == "__main__":
    main()
