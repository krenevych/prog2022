# "kaka", "k" -> "TT" : "TTaTTa"
# "" => ""
# "k" => "TT"
# "7" => "7"
# "kaka" => change("k", c, s1) + change("aka", c, s1)
pass
# def change(s, c, s1):
#     if len(s) == 0:
#         return ""
#
#     if len(s) == 1:
#         if s == c:
#             return s1
#         else:
#             return s
#
#     return change(s[0], c, s1) + change(s[1:], c, s1)

def change(s, c, s1):
    if len(s) == 0:
        return ""

    s_next = change(s[1:], c, s1)

    if s[0] == c:
        return s1 + s_next
    else:
        return s[0] + s_next



print(change("kaka", "k", "TT"))