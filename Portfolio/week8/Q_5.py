# 5. The Unix spell command is a simple spell-checker. It prints out all the words in a
# text file that are not found in a dictionary. Write and test an implementation of this,
# that takes a file name as a command-line argument.
# Note: You may want to simplify the program at first by testing with a text file that
# does not contain any punctuation. A complete version should obviously be able to
# handle normal files, with punctuation.
# Another Note: You will need a list of valid words. Linux users will already have one
# (probably in /usr/share/dict/words). It is more complicated, as usual, for
# Windows users. Happily, there are several available on GitHub.


import sys

def spell_check(file_path, dictionary_path):
    try:
        with open(dictionary_path, 'r') as dictionary_file:
            dictionary = set(word.strip().lower() for word in dictionary_file)

        with open(file_path, 'r') as file:
            words = {word.strip().lower() for line in file for word in line.split()}

            misspelled_words = words - dictionary

            if misspelled_words:
                print("Misspelled words:", *misspelled_words, sep='\n')
            else:
                print("No misspelled words found.")
    except FileNotFoundError as e:
        print(f"Error: {e.filename} not found.")


# Check if the command-line argument is provided
if len(sys.argv) != 3:
    print("Usage: python Q_5.py <demo_file_for_q5.txt> <words_alpha.txt>")
else:
    spell_check(sys.argv[1], sys.argv[2])
