"""\
    Monkey Typing

    You are given some text potentially including sensible words. You should
    count how many words are included in the given text. A word should be whole
    and may be a part of other word. Text letter case does not matter. Words
    are given in lowercase and don't repeat. If a word appears several times
    in the text, it should be counted only once.

    For example, text - "How aresjfhdskfhskd you?", words - ("how", "are", "you",
    "hello"). The result will be 3.

    Input: Two arguments. A text as a string (unicode for py2) and words as a set
    of strings (unicode for py2).

    Output: The number of words in the text as an integer.

    Example:
     count_words("How aresjfhdskfhskd you?", {"how", "are", "you", "hello"}) == 3
     count_words("Bananas, give me bananas!!!", {"banana", "bananas"}) == 2
     count_words("Lorem ipsum dolor sit amet, consectetuer adipiscing elit.",
                {"sum", "hamlet", "infinity", "anything"}) == 1

    How it is used: Python is a useful and powerful language for text processing.
    This mission is only a simple example of the kind of text searching tools you
    could build.

    Precondition:
     0 < len(text) ≤ 256
     all(3 ≤ len(w) and w.islower() and w.isalpha for w in words)
"""

def count_words(text: str, words: set) -> int:
    counter = 0
    for i in words:
        if i.lower() in text.lower():
            counter += 1

    return counter

print(count_words("How aresjfhdskfhskd you?", {"how", "are", "you", "hello"}))
print(count_words("Bananas, give me bananas!!!", {"banana", "bananas"}))
print(count_words("Lorem ipsum dolor sit amet, consectetuer adipiscing elit.", {"sum", "hamlet", "infinity", "anything"}))

# awesome