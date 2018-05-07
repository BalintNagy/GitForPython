"""\
    Secret Message

    [...]

    You are given a chunk of text. Gather all capital letters in one word in the
    order that they appear in the text.

    For example: text = "How are you? Eh, ok. Low or Lower? Ohhh.", if we collect
    all of the capital letters, we get the message "HELLO".

    Input: A text as a string (unicode).

    Output: The secret message as a string or an empty string.

    Example:
     find_message("How are you? Eh, ok. Low or Lower? Ohhh.") == "HELLO"
     find_message("hello world!") == ""
        
    How it is used: This is a simple exercise in working with strings: iterate,
    recognize and concatenate.

    Precondition:
     0 < len(text) ≤ 1000
     checkio_elementary_00_Intro.py
"""
def find_message(text: str) -> str:
    """Find a secret message"""
    msg = ""
    for i in text:
        if i.isupper():
            msg += i
    return msg


print(find_message("How are you? Eh, ok. Low or Lower? Ohhh."))
print(find_message("hello world!"))
