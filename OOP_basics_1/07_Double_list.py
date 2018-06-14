# Green Fox oop basics 1 - 7. feladat

# create a function that takes a list and returns a new list
#  with all the elements doubled

def double_list(input_list):
    doubled_list = []
    for i in input_list:
        doubled_list.append(i)
        doubled_list.append(i)
    return doubled_list

print(double_list([1, 2, 3, 4, 5]))
print(double_list([]))
