"""\
    The Most Frequent

    You have a sequence of strings, and you’d like to determine the most
    frequently occurring string in the sequence.

    Input: a list of strings.

    Output: a string.

    Example:

    most_frequent([
        'a', 'b', 'c', 
        'a', 'b',
        'a'
    ]) == 'a'
    most_frequent(['a', 'a', 'bi', 'bi', 'bi']) == 'bi'    
"""
def most_frequent(data: list) -> str:
    """
        determines the most frequently occurring string in the sequence.
    """
    most_frequent_str = ""
    count_mf = 0      # counter tök jó koncepció
    for i in list(set(data)):  # itt ugye csináltál egy 'set' objectet, aminek van egy saját count methodja,
                               # de egy ilyen típusfeladatot érdemes lenne megírni úgy, hogy nem egy beéépített funkciót használsz,
                               # hanem te implementálod annak a követését, hogy épp mi az aktuálisan legnagyobb számlálójú szó!
                               # ezeket az elementari és simple feladatokat mind érdemes lenne úgy csinálni, hogy ha még nem csináltál ilyeesmit,
                               # a basic loopokkal if-elsekkel, akkor egyszer megnézed, hogy, hogyan is lehetne a gyakorlás miatt
                               # amúgy a lista maga is egy set, annak nincs .count methodja, vagy miért kell a list és a set is?
        if data.count(i) > count_mf:
            count_mf = data.count(i)
            most_frequent_str = i
    return most_frequent_str

print(most_frequent([
        'a', 'b', 'c', 
        'a', 'b',
        'a'
    ]))
print(most_frequent(['a', 'a', 'bi', 'bi', 'bi']))   
