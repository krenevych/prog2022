def isPalindrom(s):
    return s == s[::-1]


if __name__ == '__main__':
    print(isPalindrom("assd"))
    print(isPalindrom("assa"))
