s = "Hello  Hello   Hello    World   world   hello"

wordList = s.split()
print(wordList)

wordListUnified = [word.lower() for word in wordList]
print(wordListUnified)

frequency = {} # словник частоти слів
for word in wordListUnified:
    if word not in frequency:
        frequency[word] = wordListUnified.count(word)

for word, count in frequency.items():
    print(f"слово {word} міститься в реченні {count} разів")

# print(frequency)
# print(*frequency)