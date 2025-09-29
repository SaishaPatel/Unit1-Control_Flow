# text = "Hello World"
# count = 0
# for char in text:
#     if char == "a" or char == "e" or char == "i" or char == "o" or char == "u" or char == "A" or char == "E" or char == "I" or char == "O" or char == "U":
#         count += 1
#         print(f"{count}")

text = "Hello World"
vowel_count = 0
vowels = "aeiouAEIOU"
for char in text:
    if char in vowels:
        vowel_count += 1
print(f"Vowels in '{text}': {vowel_count}")

# Part 4: Pattern Challenge A
text = "ABC123xyz"
for i in range(len(text)):
    if '0' <= text[i] <= '9':
        print(f"Digit at position {i}: {text[i]}")
        
# Part 4: Pattern Challenge B
word = "Hello"
for i in range(len(word)):
    print(f"{word[i]} at index {i} and {word[1-i]} at index {-1-i}")