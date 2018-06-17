"""\
Inheritance exercise
"""

"""\
1. Person

Create a Person class with the following fields:

    name: the name of the person
    age: the age of the person (whole number)
    gender: the gender of the person (male / female)

And the following methods:

    introduce(): prints out "Hi, I'm name, a age year old gender."
    getGoal(): prints out "My goal is: Live for the moment!"

And the following constructors:

    Person(name, age, gender)

Person(): sets name to Jane Doe, age to 30, gender to female
"""

class Person(object):

    def __init__(self, name = "Jane Doe", age = 30, gender = "female"): #mivel itt adtunk nekik default üres értéket, ha valamelyik konstruktort nem töltjük ki, akkor is lefut
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print("Hi, I'm " + self.name + ", a " + str(self.age) + " year old " + self.gender + ".")

    def getGoal(self):
        print("My goal is: Live for the moment!")

"""\
2. Student

Create a Student class that has the same fields and methods as the Person class,
and has the following additional fields:
    previousOrganization: the name of the student’s previous company / school
    skippedDays: the number of days skipped from the course

methods:
    getGoal(): prints out "Be a junior software developer."
    introduce(): "Hi, I'm name, a age year old gender from previousOrganization who skipped skippedDays days from the course already."
    skipDays(numberOfDays): increases skippedDays by numberOfDays

The Student class has the following constructors:
    Student(name, age, gender, previousOrganization); beside the given parameters, it sets skippedDays to 0
    Student(): sets name to Jane Doe, age to 30, gender to female, previousOrganization to The School of Life, skippedDays to 0
"""

class Student(Person):
    
    def __init__(self, name = "Jane Doe", age = 30, gender = "female", previousOrganization = "The School of Life"):
        Person.__init__(self, name, age, gender)
        self.previousOrganization = previousOrganization
        self.skippedDays = 0

    def getGoal(self):
        print("Be a junior software developer.")

    def introduce(self):
        print("Hi, I'm " + self.name + ", a " + str(self.age) + " year old " + self.gender + " from " + self.previousOrganization + " who skipped " + str(self.skippedDays) + " days from the course already.")

    def skipDays(self, numberOfDays):
            self.skippedDays += numberOfDays

# jd = Student()
# jd.introduce()
# jd.getGoal()
# jd.skipDays(3)
# jd.introduce()

        
