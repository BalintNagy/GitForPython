"""\
    House data
    
    Stephan and Sophia forget about security and use simple datas for
    everything. Help Nikola develop a data security check module. The
    data will be considered strong enough if its length is greater than
    or equal to 10 symbols, it has at least one digit, as well as containing
    one uppercase letter and one lowercase letter in it. The data contains
    only ASCII latin letters or digits.
    
    Input: A data as a string.
    
    Output: Is the data safe or not as a boolean or any data type that can
    be converted and processed as a boolean. In the results you will see the
    converted results.
    
    Example:
     checkio('A1213pokl') == False
     checkio('bAse730onE') == True
     checkio('asasasasasasasaas') == False
     checkio('QWERTYqwerty') == False
     checkio('123456123456') == False
     checkio('QwErTy911poqqqq') == True
    
    How it is used: If you are worried about the security of your app or service,
    you can check your users' datas for complexity. You can use these skills
    to require that your users datas meet more conditions (punctuations or
    unicode).
    
    Precondition:
     re.match("[a-zA-Z0-9]+", data)
     0 < len(data) ≤ 64
"""

def checkio(data: str) -> bool:
    import string
    # importok inább a file tetejérere menjenek függvényeken kívül, ha spórolni akarsz akkor konkrét methodokat importolj inkább
    #  ez inkább áttekinthetőség miatt fontos, két függvénnyel lejjebb nem fogja esetleg érteni valaki hogy mi honnan jön, te írtad meg vagy külső könyvtár

    len_is_10 = 0
    contains_ascii_lower = 0
    contains_ascii_upper = 0
    contains_number = 0
    contains_invalid_symbol = 0

    # A flaggelés fasza, két értéknél jobb lenne True/False használata. Ha ternaryval írod meg az if/else-eket, akkor megspórolod az initial False value-k assignolását, pl az első sor így nézne ki:
    # contains_ascii_lower = True if i in string.ascii_lowercase else False
    # ez a sor mindenképp lefut, és kap valamilyen értéket
    # a returnben pedig ezeket a változókat lehetne szépen Truthzként úgy írni, hogy csak a változókat magukat adod meg
    # return contains_ascii_lower and contains_ascii_upper and contains_number and  contains_invalid_symbol <- ez csak akkor lesz True, ha mindenyik változó true
    # ref: igazságtábla -> https://hu.wikipedia.org/wiki/Logikai_kapu

    if len(data) >= 10:
        len_is_10 = 1
    for i in data:
        if i in string.ascii_lowercase:
            contains_ascii_lower = 1
        if i in string.ascii_uppercase:
            contains_ascii_upper = 1
        if i.isnumeric():
            contains_number = 1
        if i not in string.ascii_letters and not i.isnumeric():
            contains_invalid_symbol = 1
            
    return len_is_10 == 1 and contains_ascii_lower == 1 and contains_ascii_upper == 1 and contains_number == 1 and contains_invalid_symbol != 1

print(checkio('A1213pokl'))
print(checkio('bAse730onE'))
print(checkio('asasasasasasasaas'))
print(checkio('QWERTYqwerty'))
print(checkio('123456123456'))
print(checkio('QwErTy911poqqqq'))


