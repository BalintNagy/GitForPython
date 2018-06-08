# Green Fox OOP Basics 1 - 5. feladat

# Create a `Stack` class that stores elements
# It should have a `size` method that returns number of elements it has
# It should have a `push` method that adds an element to the stack
# It should have a `pop` method that returns the last element form the stack
#  and also deletes it from it

# please don`t use the built in methods

class Stack:
    def __init__(self, elements):
        self.elements = elements
        

    def size(self):
        size = 0
        
        for i in self.elements:
            size += 1
            
        return size
    

    def push(self, new_element):
        """\
        Itt nyilván lehetne appendet használni, de a feladat kérte, hogy
        ne használjuk beépített metódusokat.
        """
        self.elements += [new_element]
        # "can only concatenate list (not "int") to list"
                
        

    def pop(self):
        if self.size() > 0:
            
            element_to_remove = self.elements[self.size() - 1]
            
            self.elements = self.elements[0:self.size() - 1]
            
            return element_to_remove
        
        else:
            
            pass

verem = Stack([1, 2, 3, 4, 5, 6, 7])
# verem = Stack([])

print(verem.size())

print(verem.pop())

print(verem.elements)

print(verem.size())

verem.push(8)

print(verem.size())

print(verem.elements)
        
            
        
