# asdf
# "a", "" - симетричні

def isSym(s):
    if len(s) <= 1:
        return True

    if s[0] != s[-1]:
        return False

    return isSym(s[1:-1])

def invert(s):
    # s = "asdf" => "fdsa"
    if len(s) <= 1:
        return s

    #        "f"  + invert("asd")
    s1 = invert(s[:-1])
    return s[-1] + s1

def change(s, c, s1):
    # s = "kaka", c = "k", s1 = "бл" => "блабла"
    if s == "":
        return ""

    change1 = change(s[1:], c, s1)

    if s[0] == c:
        return s1 + change1
    else:
        return s[0] + change1


print(change("kaka", "k", "бл"))