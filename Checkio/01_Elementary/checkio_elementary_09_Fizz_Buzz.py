"""\
    9. Fizz Buzz
       
       "Fizz buzz" is a word game we will use to teach the robots about division.
       Let's learn computers.
       
       You should write a function that will receive a positive integer and
       return:
        # "Fizz Buzz" if the number is divisible by 3 and by 5;
        # "Fizz" if the number is divisible by 3;
        # "Buzz" if the number is divisible by 5; 
        # The number as a string for other cases.

       Input: A number as an integer.

       Output: The answer as a string.

       Example:
       
        checkio(15) == "Fizz Buzz"
        checkio(6) == "Fizz"
        checkio(5) == "Buzz"
        checkio(7) == "7"
       
       How it is used: Here you can learn how to write the simplest function and
       work with if-else statements.
       
       Precondition: 0 < number ≤ 1000
"""

def checkio(number):
    if number%3 == 0 and number%5 == 0:
        result = "Fizz Buzz"
    elif number%3 == 0 and number%5 >  0:
        result = "Fizz"
    elif number%3 >  0 and number%5 == 0:
        result = "Buzz"
    else:
        result = str(number)
    return result

#     kiri. amúgy minden sorban fontos mind2 feltételre tesztelni and-el? (spoiler: nem - de, szerinted miért?)
#  visszacsatolva a kódhosszúság/performancia témára, 10,000 sornál ez 20.000 fölösleges vizsgálat e miatt lassulhat a kód, de ez nyilván nem a karakterek száma miatt van így, viszont erre lehet ilyenkor gondolni kis algoritmusoknál is
# -> hogy nagyobb datasetnél mi lesz a viselkedés

print(checkio(15))
print(checkio(6))
print(checkio(5))
print(checkio(7))
