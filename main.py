morse_dictionary = {
    'a': '._',
    'b': '_...',
    'c': '_._.',
    'd': '_..',
    'e': '.',
    'f': '.._.',
    'g': '__.',
    'h': '....',
    'i': '..',
    'j': '.___',
    'k': '_._',
    'l': '._..',
    'm': '__',
    'n': '_.',
    'o': '___',
    'p': '.__.',
    'q': '__._',
    'r': '._.',
    's': '...',
    't': '_',
    'u': '.._',
    'v': '..._',
    'w': '.__',
    'x': '_.._',
    'y': '_.__',
    'z': '__..',
    ' ': ' '
}

print("-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-")
print("-------CODE MORSE TRANSLATOR-------")
word_to_translate = input("Insert word or a phrase to translate in code morse: \n")
word_translated = []
for letter in word_to_translate:
    if letter in morse_dictionary.keys():
        word_translated.append(morse_dictionary[letter])

print("".join(word_translated))
