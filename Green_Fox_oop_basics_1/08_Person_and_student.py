# Green Fox oop basics 1 - 8. feladat

# Create a new class called `Person` that has a first_name and a last_name
#  (takes it in it's constructor)
# It should have a `greet` method that prints it's full name
 
# Create a `Student` class that is the child class of `Person`
# it should have a method to add grades
# it should have a `salute` method that prints it's full name and
# the average of it's grades as well

class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name  = last_name

    def greet(self):
        print(self.first_name + ' ' + self.last_name)

class Student(Person):
    def __init__(self, first_name, last_name):
        Person.__init__(self, first_name, last_name)
        self.grades = []
    
    def add_grade(self, grade):
        if grade in [1, 2, 3, 4, 5]:
            self.grades.append(grade)
        else:
            print('Grade can be an integer between 1 and 5! "' + str(grade) + '" cannot be added as a grade.')

    def salute(self):
        average = None
        if len(self.grades) > 0:
            average = sum(self.grades) / len(self.grades)
            # a statistics nevű modulban van mean() függvény,
            #  de nincs kedvem importálni
        print(self.first_name + ' ' + self.last_name + ', ' + str(average))

LordVoldemort = Person('Tom', 'Denem')
LordVoldemort.greet()

TheBoyWhoLived = Student('Harry', 'Potter')
TheBoyWhoLived.greet()
TheBoyWhoLived.salute()
TheBoyWhoLived.add_grade(2)
TheBoyWhoLived.add_grade(3)
TheBoyWhoLived.add_grade(7)
TheBoyWhoLived.salute()
