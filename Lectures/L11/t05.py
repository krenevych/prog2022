s = "Hello  Hello   Hello    World   world   hello"

wordList = s.split()
wordListUnified = [word.lower() for word in wordList]

frequency = {} # словник частоти слів
for word in wordListUnified:
    if word not in frequency:
        frequency[word] = wordListUnified.count(word)


max_word = ""
max_word_count = 0
for word, count in frequency.items():
    if count > max_word_count:
        max_word = word
        max_word_count = count

print(f"слово {max_word} входить до речення найбільшу кількість разів: {max_word_count}")
