# s = "1123123989"
s = "1123123989"

freq = [0] * 10
print(freq)
for c in s:
    d = int(c)
    freq[d] += 1
    # print(d)
print(freq)