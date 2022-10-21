N = int(input())

list_of_numbers = []

for item in range(0, N):
    elem = int(input())
    list_of_numbers.append(elem)

for i in range(0, N // 2):
    list_of_numbers[i], list_of_numbers[N-1-i] = list_of_numbers[N-1-i], list_of_numbers[i]

print(*list_of_numbers)