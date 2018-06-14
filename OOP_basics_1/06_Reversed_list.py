# Green Fox OOP Basics 1 - 6. feladat

# create a function that takes a list and returns a new list that is reversed

def reversed_list(list):
    reversed_list = []
    for i in range(0, len(list)):
        index = len(list) - i - 1
        reversed_list.append(list[index])
    return reversed_list

print(reversed_list([1, 2, 3, 4]))                  
