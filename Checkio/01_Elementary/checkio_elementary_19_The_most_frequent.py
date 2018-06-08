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
    count_mf = 0
    for i in list(set(data)):
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
