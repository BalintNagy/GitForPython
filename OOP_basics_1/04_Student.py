# Green Fox OOP Basics 1 - 4. feladat

# Create a student Class
# that has a method `add_grade`, that takes a grade from 1 to 5
# an other method `get_average`, that returns the average of the
# grades

class student:
    def __init__(self):
        self.grades = []

    def add_grade(self, grade):
        if grade in [1, 2, 3, 4, 5]:
            self.grades.append(grade)
        else:
            print('Grade can be an integer between 1 and 5! "' + str(grade) + '" cannot be added as a grade.')

    def get_average(self):
        return sum(self.grades) / len(self.grades)
        # a statistics modulban van mean() függvény, de nincs kedvem importálni

Anselmus = student()

# Megíratunk vele 5 dolgozatot:
for i in range(1, 6):
    Anselmus.add_grade(i)

Anselmus.add_grade(7)

# Mennyi lett az átlaga?
print(Anselmus.get_average())

# Amúgy milyen jegyeket kapott?
print(Anselmus.grades)
