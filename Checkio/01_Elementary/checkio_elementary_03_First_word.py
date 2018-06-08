"""\
    3. First Word
       You are given a string where you have to find its first word.

       When solving a task pay attention to the following points:
           There can be dots and commas in a string.
           A string can start with a letter or, for example, a dot or space.
           A word can contain an apostrophe and it's a part of a word.
           The whole text can be represented with one word and that's it.
       
       Input: A string.

       Output: A string.

       Example:

           first_word("Hello world") == "Hello"
           first_word("greetings, friends") == "greetings"

       How it is used: the first word is a command in a command line

       Precondition: the text can contain a-z A-Z , . '                                    
"""
def first_word(text: str) -> str:
    """
        returns the first word in a given text.
    """
    import string

    szoelemek = string.ascii_letters + "'"
    i = 0
    start = 0
    end = 0
    
    for i in range(0, len(text)):
        if text[i] in szoelemek:
            start = i
            break
    
    for i in range(start+1, len(text)):
        if not text[i] in szoelemek:
            end = i
            break
    
    if end == 0:
        end = len(text) #Ez azért kell, mert ha az első szó végén vége a stringnek, a második for-ciklusban az if sosem lesz igaz.
        
    return text[start:end]