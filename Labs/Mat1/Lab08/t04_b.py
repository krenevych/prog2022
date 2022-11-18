

def inv(s):
    # "asd" => "dsa"
    if s == "":
        return s

    return s[-1] + inv(s[:-1])

print(inv("asdf"))

