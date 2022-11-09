# s = "1123123989"
s = 1123123989

freq = [0] * 10
print(freq)
while s > 0:
    d = s % 10
    freq[d] += 1
    s = s // 10
    # print(d)
print(freq)