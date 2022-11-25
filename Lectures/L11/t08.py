s = "Hello  Hello   Hello    World   world   hello"

wordList = s.split()
wordListUnified = [word.lower() for word in wordList]

frequency = {} # словник частоти слів
for word in set(wordListUnified):
    frequency[word] = wordListUnified.count(word)

for word, count in frequency.items():
    print(f"слово {word} міститься в реченні {count} разів")

# print(frequency)
# print(*frequency)