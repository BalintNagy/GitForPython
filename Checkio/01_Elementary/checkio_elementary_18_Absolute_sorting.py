"""\
    Absolute sorting

    Let's try some sorting. Here is an array with the specific rules.

    The array (a tuple) has various numbers. You should sort it, but sort it by
    absolute value in ascending order. For example, the sequence
    (-20, -5, 10, 15) will be sorted like so: (-5, 10, 15, -20).
    Your function should return the sorted list or tuple.

    Precondition: The numbers in the array are unique by their absolute values.
    
    Input: An array of numbers , a tuple..

    Output: The list or tuple (but not a generator) sorted by absolute values
    in ascending order.

    Addition: The results of your function will be shown as a list in the tests
    explanation panel.

    Example:
     checkio((-20, -5, 10, 15)) == [-5, 10, 15, -20] # or (-5, 10, 15, -20)
     checkio((1, 2, 3, 0)) == [0, 1, 2, 3]
     checkio((-1, -2, -3, 0)) == [0, -1, -2, -3]

    How it is used: Sorting is a part of many tasks, so it will be useful to
    know how to use it.

    Precondition: len(set(abs(x) for x in array)) == len(array)
     0 < len(array) < 100
     all(isinstance(x, int) for x in array)
     all(-100 < x < 100 for x in array)
"""
def checkio(numbers_array: tuple) -> list:
    print(numbers_array)
    numbers_dict = {}
    # negorpos = 0 (ezt kikommenteltem, mégis  múködik a kód, miért?)
    list_to_return = []
    for i in numbers_array:
        if i < 0:
            negorpos = -1
        else:
            negorpos =  1
        numbers_dict[abs(i)] = negorpos
    
    sorted_by_abs = sorted(numbers_dict.keys())
    
    for i in sorted_by_abs:
        list_to_return.append(i * numbers_dict[i])
        
    return list_to_return
    # Szépséghiba: alapvetően tuple-t kellett volna returnölni, én viszont
    #              listet returnölök.

    # "convert" vagy még inkább "cast" címszavak ilyenkor hasznosak kereséshez, az nem para ha belül más adatruktóraként
    # kezeled, de az output-ra gondolj úgy mint egy interfészre amiben megegyezel egy másik programozóval,
    # és ő úgy dolgozik, hogy azt az  adattípust várja majd ahhoz amin ő dolgozik

    # első függvényt szintén érdemes lecsekkolni: https://docs.python.org/3/library/functions.html
print(checkio((-20, -5, 10, 15)))
print(checkio((1, 2, 3, 0)))
print(checkio((-1, -2, -3, 0)))
