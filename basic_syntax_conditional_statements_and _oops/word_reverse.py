# Get a word as input from the user
word = input()
# empty string to store the reversed word

reversed_word = ""
# Loop through the word in reverse order
for i in range(len(word) - 1, -1, -1):
  # Extract each character of the word in reverse order and add it to the reversed_word string
  reversed_word += word[i]
print(reversed_word)