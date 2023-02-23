'''
Program: Language Translation
Author: Lisa Klinbuayam
Purpose: To translate the word from one language to another (English or French).
Revision:
    00: Prompting, and checking user input
    01: Using continue loop to check the input and ask to add
    02: Checking if the word to add is in English or either French otherwise invalid
'''

# Announcement
print('Program to translate words from English to French and vice-versa')

# Create lists of words
english = ['chicken', 'salt', 'apple', 'hi', 'house', 'clock', 'winter']
french = ['poulet', 'sel', 'pomme', 'bonjour', 'maison', 'horloge', 'hiver']


# Define function to receive prompt(in below) and convert into a lower case
def input_lower(prompt):
    return input(prompt).lower()


# Use continue loop and check if the word input is in the list otherwise add or exit
while True:
    word = input_lower('\nEnter an English or French word to translate: ')
    if word == '':
        print('Exiting ...')
        break

    if word in english:
        english_index = english.index(word)  # Using index to check corrytfesponding word
        print(f"The English word '{word}' is '{french[english_index]}' in French")
        continue

    elif word in french:
        french_index = french.index(word)  # Using index to check corresponding word
        print(f"The French word '{word}' is '{english[french_index]}' in English")
        continue

    # No translation found, propose to add it
    print(f"The word '{word}' was not found in English or French word lists")
    should_add_word = None
    while should_add_word not in ['y', 'n']:
        should_add_word = input_lower(f"Would you like to add '{word}' to the lists? <y>es or <n>o ")
        if should_add_word == 'n':
            continue

        original_language = None
        while original_language not in ['e', 'f']:  # Prompting user for selecting to add in language
            original_language = input_lower(f"What language is '{word}' in? <E>nglish or <F>rench ")

            if original_language == 'e':  # if word in English, French will be added
                translated_word_to_add = input_lower(f"What is the French word for '{word}'? ")
                english.append(word)
                french.append(translated_word_to_add)
            elif original_language == 'f':  # if word in French, English will be added
                translated_word_to_add = input_lower(f"What is the English word for '{word}'? ")
                french.append(word)
                english.append(translated_word_to_add)
            else:
                print('Invalid language')