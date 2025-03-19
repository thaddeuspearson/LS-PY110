"""
Create a function that takes a string argument and returns a copy of the
string with every second character in every third word converted to uppercase.
Other characters should remain the same.
P
    inputs: str
    outputs: str
    rules:
        Explicit Reqs:
            - accept a str
            - retutrn a str
            - return str should have every second char uppercase in every
              third word
            - Do not modify any other word
        Implicit Reqs:
            - an empty string returns an enpty str
            - third words of len less than 2 stay the same
E
    original = 'Lorem Ipsum is simply dummy text of the printing world'
    expected = 'Lorem Ipsum iS simply dummy tExT of the pRiNtInG world'
    assert to_weird_case(original) == expected

    original = 'It is a long established fact that a reader will be distracted'
    expected = 'It is a long established fAcT that a rEaDeR will be dIsTrAcTeD'
    assert to_weird_case(original) == expected

    assert to_weird_case('aaA bB c') == 'aaA bB c'

    original = "Mary Poppins' favorite word is supercalifragilisticexpialidocious"
    expected = "Mary Poppins' fAvOrItE word is sUpErCaLiFrAgIlIsTiCeXpIaLiDoCiOuS"
    assert to_weird_case(original) == expected
D
    list
A
    - split the string into a word_list
    - loop through words counting by 3
        - loop through each third word
            - create a new_str
            - if index of the curr char is odd, append the curr char upprcased
            - else concat the curr char as is
    - return the word list joined with a space
C
"""


def alternate_case(word: str) -> str:
    """Returns the given word with every second char capitalized"""
    new_str = ""

    for i, c in enumerate(word):
        new_str += c.upper() if i % 2 == 1 else c


def to_weird_case(original: str) -> str:
    """
    Returns the given string with every third word having every other letter
    uppercase
    """
    words = original.split(" ")

    for third_word_idx in range(2, len(words), 3):
        words[third_word_idx] = alternate_case(words[third_word_idx])

    return " ".join(words)


if __name__ == "__main__":
    original = 'Lorem Ipsum is simply dummy text of the printing world'
    expected = 'Lorem Ipsum iS simply dummy tExT of the pRiNtInG world'
    assert to_weird_case(original) == expected

    original = 'It is a long established fact that a reader will be distracted'
    expected = 'It is a long established fAcT that a rEaDeR will be dIsTrAcTeD'
    assert to_weird_case(original) == expected

    assert to_weird_case('aaA bB c') == 'aaA bB c'

    original = "Mary Poppins' favorite word is supercalifragilisticexpialidocious"
    expected = "Mary Poppins' fAvOrItE word is sUpErCaLiFrAgIlIsTiCeXpIaLiDoCiOuS"
    assert to_weird_case(original) == expected
