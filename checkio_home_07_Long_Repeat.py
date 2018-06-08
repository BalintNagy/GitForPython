"""\
    Long Repeat

    Here you should find the length of the longest substring that consists of
    the same letter. For example, line "aaabbcaaaa" contains four substrings
    with the same letters "aaa", "bb","c" and "aaaa". The last substring is the
    longest one which makes it an answer.

    Input: String.

    Output: Int.

    Example:
     long_repeat('sdsffffse') == 4
     long_repeat('ddvvrwwwrggg') == 3

     long_repeat('') == 0
     long_repeat('abababa') == 1
"""
def long_repeat(line):
    """
        length the longest substring that consists of the same char
    """
    counter = 1
    len_longest = 1
    for i in range(1, len(line)):
        if line[i] == line[i-1]:
            counter += 1 # Counter++ is lehetne, de azt az IDLE nem érti...
            if counter > len_longest:
                len_longest = counter
        else:
            counter = 1
        
    if len(line) == 0: # Ezt nem érzem túl elegánsnak.
        return 0
    return len_longest

# Ez kapcsolódik a Truthy-Falsy témához ami egyszer feljött azzal kapcsolatban, hogy runtime bizonyos értékek felvehetnek "True" v "False" valuet kiértékeléskor.
# Ebben az esetben azt kell látni, hogy az if után, egy kifejezés következik, ami mind1, hogy miből áll vagy milyen hosszú, egy darab True v False booleanként fog visszatérni
# De használhatunk változókat is önmagukban való kiértékelésre (ez a truthy-falsy), pl "if list:"
# Shellben a (bool()) függvénnyel tudod megnézni, hogy egy kifejezésként való kiértékeléskor mivé konvertálódik egy változó.

# >>> line = []
# >>> bool(line)
# False
# >>> bool(len(line))
# False
# >>> line = [1, 2]
# >>> bool(len(line))
# True
# >>> bool(line)
# True
# >>>

# A mostani kódodba nem kell a bool() fv., mert a python a if után kiértékelendő dolgokra számít,
# de egyéb iránt érdemes megjegyezni és ha van lehetőség rá akkor használni ugyanúgy mint egy str() vagy egy int() konverziót csak pl flaggekhez

print(long_repeat('sdsffffse'))
print(long_repeat('ddvvrwwwrggg'))

print(long_repeat(''))
print(long_repeat('abababa'))
