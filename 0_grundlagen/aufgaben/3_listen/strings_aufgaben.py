"""
Write a Python function that takes a list of words
 and return the longest word and the length of the longest one.
 List contains minimum one word

Sample Output:
Longest word: Exercises
Length of the longest word: 9
"""

words_list = ["Exercises", "Exercise9", "kanal", "pp", "Exercis"]
index = 0
for i, n in enumerate(words_list):
    if len(n) > len(words_list[index]):
        index = i

print(f"Longest word: {words_list[index]}")
print(f"Length: {len(words_list[index])}")
