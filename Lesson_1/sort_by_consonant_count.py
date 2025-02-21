"""PEDAC

Problem:
    Given a list of strings, sort the list based on the highest number of
    adjacent consonants a string contains and return the sorted list.

    Input:
        - list of strings
    Output:
        - list of strings sorted as required

    Explicit Rules:
        - If two strings contain the same highest number of adjacent
        consonants, they should retain their original order in relation to
        each other.
        - Consonants are considered adjacent if:
            - they are next to each other in the same word
            - if there is a space between two consonants in adjacent words.

    Implicit Rules:
        - Sort the list in decending order

    Clarifying Questions:
        - Will the input list only have strings as elements? yes
        - Do we need to account for international characters? no
        - account for case? no

Example/Test Cases:
    ['aa', 'baa', 'ccaa', 'dddaa']
    -> ['dddaa', 'ccaa', 'aa', 'baa']

    ['can can', 'toucan', 'batman', 'salt pan']
    -> ['salt pan', 'can can', 'batman', 'toucan']

    ['bar', 'car', 'far', 'jar']
    -> ['bar', 'car', 'far', 'jar']

    ['day', 'week', 'month', 'year']
    -> ['month', 'day', 'week', 'year']

    ['xxxa', 'xxxx', 'xxxb']
    -> ['xxxx', 'xxxb', 'xxxa']

Data Structure:
    A lookup dictionary will help to sort efficiently, with the keys being
    ints and the values being lists, where the words with the longest
    consonant substring can be pushed in order of occurance


Algorithm:
    - loop through the word list
    - find the longest consecutive contant substring in the curr word
        - create a max_consonant variable
        - create a curr consonant counter
        - remove any spaces in the current word
        - loop through characters
            - if the curr char is a vowel
                - if the curr word consonant counter is gt max_consonant
                    - reassign max_consonant to curr_word_consonent_count
                    - reset curr_consonant count
                - else increment the curr_consonant counter
        - return max_consonant_count
    - push the word to a corresponding max_consonant int key in the lookup
    dictionary
    - sort the dictionary by key in decending order
    - concatenate the lookup value lists together and return
"""


def get_max_adjacent_consonant_count(word):
    max_consonant_count = 0
    curr_consonant_count = 0
    word = ''.join(word.split())

    for c in word:
        if c.lower() in "aeiou":
            max_consonant_count = max(max_consonant_count,
                                      curr_consonant_count)
            curr_consonant_count = 0
        else:
            curr_consonant_count += 1

    max_consonant_count = max(max_consonant_count, curr_consonant_count)
    return max_consonant_count if max_consonant_count > 1 else 0


def sort_by_consonant_count(word_list):
    lookup = {}
    sorted_words = []

    for word in word_list:
        max_adjacent_consonants = get_max_adjacent_consonant_count(word)
        max_adjacent_consonant_words = lookup.setdefault(
                                                max_adjacent_consonants, [])
        max_adjacent_consonant_words.append(word)

    sorted_lookup_keys = sorted(lookup.keys(), reverse=True)

    for k in sorted_lookup_keys:
        sorted_words.extend(lookup[k])
    return sorted_words


my_list = ['aa', 'baa', 'ccaa', 'dddaa']
print(sort_by_consonant_count(my_list) == ['dddaa', 'ccaa', 'aa', 'baa'])

my_list = ['can can', 'toucan', 'batman', 'salt pan']
print(sort_by_consonant_count(my_list) == ['salt pan', 'can can',
                                           'batman', 'toucan'])

my_list = ['bar', 'car', 'far', 'jar']
print(sort_by_consonant_count(my_list) == ['bar', 'car', 'far', 'jar'])

my_list = ['day', 'week', 'month', 'year']
print(sort_by_consonant_count(my_list) == ['month', 'day', 'week', 'year'])

my_list = ['xxxa', 'xxxx', 'xxxb']
print(sort_by_consonant_count(my_list) == ['xxxx', 'xxxb', 'xxxa'])
