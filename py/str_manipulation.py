#STRING MANIPULATION

single_quote = 'This is a string with single quotes and it can contain "double quotes" without any issues.'
double_quote = "This is a string with double quotes and it can contain 'single quotes' without any issues."
multi_line_string = """This is a multi-line string that can span across multiple lines.
It can contain both 'single quotes' and "double quotes" without any issues."""

#string indexing and slicing
#indexing: accessing individual characters in a string using their position (index)
#slicing: extracting a portion of a string using a range of indices

text = "Hello, World!"
print(text)
print(text[0]) # first character, result: H
print(text[7]) # eighth character, result: W
print(text[-1]) # last character, result: !
print(text[0:5]) # substring from index 0 to 4, result: Hello
print(text[7:12]) # substring from index 7 to 11, result: World

#string methods

name = "Alice Wonderland"

print(name.upper()) # convert to uppercase, result: ALICE WONDERLAND
print(name.lower()) # convert to lowercase, result: alice wonderland
print(name.capitalize()) # capitalize first letter, result: Alice wonderland
print(name.replace("A", "E")) # replace A with E, result: Elice
print(len(name)) # length of the string, result: 13
print(name.title()) # title case, result: Alice Wonderland

#string formatting

animal = "fish"
number = 5

#results are the same
# using f-string
print(f"I have {number} {animal}s.")

# using format method
print("I have {} {}s.".format(number, animal))

# using % operator
print("I have %d %ss." % (number, animal))