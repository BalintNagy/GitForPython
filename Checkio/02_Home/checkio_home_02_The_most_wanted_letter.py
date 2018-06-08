"""\
    The Most Wanted Letter

    You are given a text, which contains different english letters and
    punctuation symbols. You should find the most frequent letter in the text.
    The letter returned must be in lower case.
    While checking for the most wanted letter, casing does not matter, so for
    the purpose of your search, "A" == "a". Make sure you do not count
    punctuation symbols, digits and whitespaces, only letters.

    If you have two or more letters with the same frequency, then return the
    letter which comes first in the latin alphabet. For example -- "one"
    contains "o", "n", "e" only once for each, thus we choose "e".

    Input: A text for analysis as a string.

    Output: The most frequent letter in lower case as a string.

    Example:
     checkio("Hello World!") == "l"
     checkio("How do you do?") == "o"
     checkio("One") == "e"
     checkio("Oops!") == "o"
     checkio("AAaooo!!!!") == "a"
     checkio("abe") == "a"

    How it is used: For most decryption tasks you need to know the frequency of
    occurrence for various letters in a section of text. For example: we can
    easily crack a simple addition or substitution cipher if we know the
    frequency in which letters appear. This is interesting stuff for language
    experts!

    Precondition:
     A text contains only ASCII symbols.
     0 < len(text) ≤ 10^5
"""

def checkio(text: str) -> str:
    import string
    most_frequent_letter = ''
    count_mf = 0
    for i in sorted(set(list(text.lower())), reverse = True):
    # Azért kell a sorted és a reverse, hogy holtverseny esetén az abc-ben korábbi betűt értékelje ki később.
        if i in string.ascii_letters:
            if text.lower().count(i) >= count_mf:
                count_mf = text.lower().count(i)
                most_frequent_letter = i
    return most_frequent_letter

print(checkio("Hello World!"))
print(checkio("How do you do?"))
print(checkio("One"))
print(checkio("Oops!"))
print(checkio("AAaooo!!!!"))
print(checkio("abe"))
