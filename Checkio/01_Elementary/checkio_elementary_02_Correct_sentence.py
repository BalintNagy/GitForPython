"""\
    2. Correct Sentence
       For the input of your function will be given one sentence. You have to return its fixed copy in a way so it’s always starts with a capital letter and ends with a dot.

       Pay attention to the fact that not all of the fixes is necessary. If a sentence already ends with a dot then adding another one will be a mistake.

       Input: A string.

       Output: A string.

       Precondition: No leading and trailing spaces, text contains only spaces, a-z A-Z , and .
"""
def correct_sentence(text: str) -> str:
    """
        returns a corrected sentence which starts with a capital letter
        and ends with a dot.
    """
    # ha nem írsz semmit az else ágra, az olyan mintha azt írnád:
    #else:
        # continue
    # Az ilyen über egyszerű 1-2 szavas if/else-eket a legszebb megírni egy un. 'ternary operatorral'

    text = text[0].upper() + text[1:]
    if text[-1] != ".":
        text += "."
    return text