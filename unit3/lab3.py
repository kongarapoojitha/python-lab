
# Frequency Counter Using Dictionaries

sentence = input("Enter a sentence: ")

words = sentence.lower().split()

frequency = {}

for word in words:
    frequency[word] = frequency.get(word, 0) + 1

print("\n===== WORD FREQUENCY COUNTER =====")

for word, count in frequency.items():
    print(word, ":", count)

print("\nTotal Words:", len(words))
print("Unique Words:", len(frequency))
