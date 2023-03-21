# 0  1  2  3  4  5  6
# 0! 1! 2! 3! 4! 5! 6!
# 1  1  2  6  24 120...

# N = 5

# n = 0
# while n <= N:
#     n += 1
#     an = n * an

def fact_gen(N):
    an = 1
    yield an
    for n in range(1, N+1):
        an = n * an
        yield an

def fact_gen_to_inf():
    an = 1
    n = 0
    yield an
    while True:
        n += 1
        an = n * an
        yield an


if __name__ == '__main__':

    for f in fact_gen_to_inf():
        if f > 1000_000:
            break
        print(f)
