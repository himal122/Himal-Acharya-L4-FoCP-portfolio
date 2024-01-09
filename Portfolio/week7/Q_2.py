# 2. Write and test three functions that each take two words (strings) as parameters and
# return sorted lists (as defined above) representing respectively:
# Letters that appear in at least one of the two words.
# Letters that appear in both words.
# Letters that appear in either word, but not in both.


def letters_in_either(word1, word2):
    # Use set union to get letters in at least one of the words
    letters_set = set(word1) | set(word2)
    
    # Convert the set to a sorted list
    sorted_letters_list = sorted(list(letters_set))
    
    return sorted_letters_list

def letters_in_both(word1, word2):
    # Use set intersection to get letters in both words
    letters_set = set(word1) & set(word2)
    
    # Convert the set to a sorted list
    sorted_letters_list = sorted(list(letters_set))
    
    return sorted_letters_list

def letters_in_either_not_both(word1, word2):
    # Use set symmetric difference to get letters in either word, but not in both
    letters_set = set(word1) ^ set(word2)
    
    # Convert the set to a sorted list
    sorted_letters_list = sorted(list(letters_set))
    
    return sorted_letters_list

# Example usage:
word1 = "hello"
word2 = "world"

result_either = letters_in_either(word1, word2)
result_both = letters_in_both(word1, word2)
result_either_not_both = letters_in_either_not_both(word1, word2)

print(f"Letters in either word: {result_either}")
print(f"Letters in both words: {result_both}")
print(f"Letters in either, but not in both: {result_either_not_both}")
