"""\
    All the Same

    In this mission you should check if all elements in the given list are equal.

    Input: List.

    Output: Bool.

    Example:

     all_the_same([1, 1, 1]) == True
     all_the_same([1, 2, 1]) == False
     all_the_same(['a', 'a', 'a']) == True
     all_the_same([]) == True

    Precondition: all elements of the input list are hashable    
"""
from typing import List, Any

def all_the_same(elements: List[Any]) -> bool:
    counter = 1
    for i in range(1, len(elements)):
        if elements[i] == elements[i - 1]:
            counter += 1
    if len(elements) == 0:
        return True
    return counter == len(elements)

print(all_the_same([1, 1, 1]))
print(all_the_same([1, 2, 1]))
print(all_the_same(['a', 'a', 'a']))
print(all_the_same([]))
