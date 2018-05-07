"""\
    1. Say hi
       In this mission you should write a function that introduce a person with a given parameters in attributes.

        Input: Two arguments. String and positive integer.

        Output: String.

        Example:
                say_hi("Alex", 32) == "Hi. My name is Alex and I'm 32 years old"
                say_hi("Frank", 68) == "Hi. My name is Frank and I'm 68 years old"
"""
def say_hi(name, age):
    """
        Hi!
    """
    # your code here
    return "Hi. My name is " + name + " and I'm " + str(age) + " years old"

szoveg = say_hi("Frank", 68)
print(szoveg)