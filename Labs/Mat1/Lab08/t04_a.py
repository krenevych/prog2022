def isSym(s):
    # "a", "" => True
    # "asdsa"

    if len(s) <= 1:
        return True

    if s[0] != s[-1]:
        return False

    return isSym(s[1:-1])

res = isSym("asdsa")
print(res)

# isSym("asdsa") = "a" == "a" and isSym("sds")
#                                     ||
#                                     "s" == "s" and isSym("d")
#                                                       ||
#                                                      True

# isSym("asdRa") = "a" == "a" and isSym("sdR")
#                                     ||
#                                     "s" == "R" and isSym("d")
#
