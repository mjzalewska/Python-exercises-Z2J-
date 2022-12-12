"""
Challenge 4.9
Write a program called translate.py that asks the user for some input with the following prompt:
"Enter some text: "
Use .replace() to convert the text entered by the user into leetspeak by making the following changes to
lowercase letters:

- the letter a becomes 4
- the letter b becomes 8
- the letter e becomes 3
- the letter l becomes 1
- the letter o becomes 0
- the letter s becomes 5
- the letter t becomes 7

Your program should then display the resting string as output.
"""
dictionary = {'a': '4', 'b': '8', 'e': '3', 'l': '1', 'o': '0', 's': '5', 't': '7'}
user_input = input("Enter some text: ")
new_string = ""
for char in user_input:
    if char in dictionary.keys():
        new_string += dictionary[char]
    else:
        new_string += char

print(new_string)


