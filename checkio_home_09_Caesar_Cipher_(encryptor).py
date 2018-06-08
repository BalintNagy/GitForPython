"""\
    Caesar Cipher (encryptor)

    Your mission is to encrypt a secret message (text only, without special
    chars like "!", "&", "?" etc.) using Caesar cipher where each letter of
    input text is replaced by another that stands at a fixed distance.
    For example ("a b c", 3) == "d e f"

    Input: A secret message as a string (lowercase letters only and white
    spaces)

    Output: The same string, but encrypted

    Example:
     to_encrypt("a b c", 3) == "d e f"
     to_encrypt("a b c", -3) == "x y z"
     to_encrypt("simple text", 16) == "iycfbu junj"
     to_encrypt("important text", 10) == "swzybdkxd dohd"
     to_encrypt("state secret", -13) == "fgngr frperg"

    How it is used: For cryptography and to save important information.

    Precondition:
       0 < len(text) < 50
     -26 < delta     < 26
"""

def to_encrypt(text, delta):
    import string
    alphabet = string.ascii_lowercase
    text2 = ''
    for i in text:
        if i == ' ':
            text2 += ' '
        else:
            if alphabet.index(i) + delta > len(alphabet) - alphabet.index(i):
                text2 += alphabet[delta - (len(alphabet) - alphabet.index(i))]
            else:
                text2 += alphabet[alphabet.index(i) + delta]
    
    return text2


print(to_encrypt("a b c", 3))
print(to_encrypt("a b c", -3))
print(to_encrypt("simple text", 16))
print(to_encrypt("important text", 10))
print(to_encrypt("state secret", -13))
