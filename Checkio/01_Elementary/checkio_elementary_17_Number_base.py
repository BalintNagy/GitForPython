"""\
    Number Base

    Do you remember the radix and Numeral systems from math class? Let's
    practice with it.

    You are given a positive number as a string along with the radix for it.
    Your function should convert it into decimal form. The radix is less than
    37 and greater than 1. The task uses digits and the letters A-Z for the
    strings.

    Watch out for cases when the number cannot be converted. For example: "1A"
    cannot be converted with radix 9. For these cases your function should
    return -1.

    Input: Two arguments. A number as string and a radix as an integer.

    Output: The converted number as an integer.

    Example:
     checkio("AF", 16) == 175
     checkio("101", 2) == 5
     checkio("101", 5) == 26
     checkio("Z", 36) == 35
     checkio("AB", 10) == -1

    How it is used: Here you will learn how to work with the various numeral
    systems and handle exceptions.

    Precondition: 
     re.match("\A[A-Z0-9]\Z", str_number)
     0 < len(str_number) ≤ 10
     2 ≤ radix ≤ 36
"""
def checkio(str_number: str, radix: int) -> int:
    """\
        Kértem egy hintet, ezt kaptam:
        "Don't try to reinvent the bicycle and use int() conversion. Python
         already has a tool to convert a number between various number bases.
        
         int("1A", 16) == 170
         int("101", 2) == 5"
    """
    try:
        return int(str_number, radix)
    except ValueError:
        return -1
    # ---> Ez így nagyon egyszerű a tanács alapján, és működik, de milyen
    #      számokat és milyen logika alapján jelölnek ezek a betűket (is)
    #      tartalmazó stringek?!
    # ---> Oké, megértettem, hogy az "AF", az pl. egy hexadecimális izé.
    #      (https://owlcation.com/stem/Convert-Hex-to-Decimal) De még mindig
    #      nem tiszta, hogy ez hogy működik, és mire jó. Meg hogy pl. mi a "Z".

print(checkio("AF", 16))
print(checkio("101", 2))
print(checkio("101", 5))
print(checkio("Z", 36))
print(checkio("AB", 10))
