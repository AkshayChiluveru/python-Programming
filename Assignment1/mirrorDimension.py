word = input("Input: ")
reverse_word = ""
i = len(word) -1
while i >= 0:
    reverse_word += word[i]
    i -= 1
print("Output:", reverse_word)