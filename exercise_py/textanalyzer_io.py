#text = input("Enter a string: ")

text = """Python is a powerful programming language. It's easy to learn and versatile!
You can use it for web development, data science, and automation. The syntax is clean and readable.
Ths makes Python a great choice for beginners and experienced developers alike."""

# Count the number of characters in the string
char_count = len(text)

#count the number of words in the string
word_count = len(text.split())

#count number of sentences in the string
sentence_count = text.count('.') + text.count('!') + text.count('?')

print(f"String: {text}")
print(f"Character count: {char_count}")
print(f"Word count: {word_count}")
print(f"Sentence count: {sentence_count}")