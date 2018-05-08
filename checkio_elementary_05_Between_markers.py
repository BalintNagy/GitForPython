"""\
    5. Between Markers

       You are given a string and two markers (the initial and final). You have
       to find a substring enclosed between these two markers. But there are a
       few important conditions:

        # The initial and final markers are always different.
        # If there is no initial marker then the beginning should be considered
          as the beginning of a string.
        # If there is no final marker then the ending should be considered as the
          ending of a string.
        # If the initial and final markers are missing then simply return the 
          whole string.
        # If the final marker is standing in front of the initial one then return
          an empty string.

       Input: Three arguments. All of them are strings. The second and third
       arguments are the initial and final markers.

       Output: A string.

       Example:

        between_markers('What is >apple<', '>', '<') == 'apple'
        between_markers('No[/b] hi', '[b]', '[/b]') == 'No'

       How it is used: for parsing texts

       Precondition: can't be more than one final marker and can't be more than
       one initial
"""

def between_markers(text: str, begin: str, end: str) -> str:
    """
        returns substring between two given markers
    """

    if begin in text:
        after_begin = text.split(begin)
    else:
        after_begin = []
        after_begin.append("")
        after_begin.append(text)

    if end in after_begin[1]:
        before_end = after_begin[1].split(end)
    else:
        before_end = []
        before_end.append(after_begin[1])

    # Az alábbi if-else rész oldja meg azt a feltételt, hogy 'ha az end a begin előtt van a textben, akkor üres stringet
    # adjon vissza':
    if end in after_begin[0]:
        return ""
    else:
        return before_end[0]
    
print(between_markers('What is >apple<', '>', '<'))
print(between_markers("<head><title>My new site</title></head>", "<title>", "</title>"))
print(between_markers('No[/b] hi', '[b]', '[/b]'))
print(between_markers('No [b]hi', '[b]', '[/b]'))
print(between_markers('No hi', '[b]', '[/b]'))
print(between_markers('No <hi>', '>', '<'))
print(between_markers("No <hi> one",">","<"))

# .find() .index() :)