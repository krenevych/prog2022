s = input()
# s = "9*8+76-54//3+2**10"

i = 0
counter = 0
while i < len(s):
    # print(s[i])
    if s[i] in "+-*%/":
        counter += 1
        if s[i] == "*" and s[i + 1] == "*":
            i += 1
        elif s[i] == "/" and s[i + 1] == "/":
            i += 1
    i += 1

print(counter)
