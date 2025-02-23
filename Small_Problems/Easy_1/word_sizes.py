"""
Write a function that takes a string consisting of zero or more space
separated words and returns a dictionary that shows the number of words of
different sizes. Words consist of any sequence of non-space characters.
"""
import sys


def word_sizes(words=None):
    """Returns a dictionary mapping the count of words of each word length in
    the given words string.

    :param words (str): the words to map to their respective lengths
    :returns word_lengths_dict (dict): the mapping of word lengths to count of
    words with the respective length
    """
    if words is None:
        words = input("Please enter a string: ")

    word_lengths_dict = {}

    for word in words.split():
        word = "".join([c for c in word if c.isalnum()])
        word_len = len(word)
        word_lengths_dict.setdefault(word_len, 0)
        word_lengths_dict[word_len] += 1

    return word_lengths_dict


# pylint: disable=pointless-string-statement
"""CODE EXPLAINATION
word_sizes is defined on line 9 and has 1 parameter, words, which accepts a
string.

The conditional check on line 17 checks to see if any argument has been passed
to word_sizes, and prompts the user to enter a string if not.

on line 20, a local variable word_lengths_dict is instantiated to an empty
dict literal.

The loop on line 22 iterates through each individual word in words. Within
each loop execution, word is striped of all non alphanumeric characters,
word_len is assigned to the value of the length of the current word, which is
then checked or set as a key in word_length_dict with the setdefault method,
and the value at that respective key is incremented by 1 on line 26.

word_lengths_dict is returned on line 27.
"""


# Test Cases
if __name__ == "__main__":
    args = sys.argv[1:]
    if args and args[0] == "test":
        # pylint: disable=invalid-name
        string = 'Four score and seven.'
        assert word_sizes(string) == {4: 1, 5: 2, 3: 1}

        string = 'Hey diddle diddle, the cat and the fiddle!'
        assert word_sizes(string) == {3: 5, 6: 3}

        string = 'Humpty Dumpty sat on a w@ll'
        assert word_sizes(string) == {6: 2, 3: 2, 2: 1, 1: 1}

        string = "What's up doc?"
        assert word_sizes(string) == {5: 1, 2: 1, 3: 1}

        assert not word_sizes('')
    else:
        print(word_sizes())
