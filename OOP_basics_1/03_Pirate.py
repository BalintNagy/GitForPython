# Green Fox OOP Basics 1 - 3. feladat

# create a pirate class
# it should have 2 methods
# drink_rum()
# hows_goin_mate()
# if the drink_rum was called at least 5 times:
# hows_goin_mate should return "Arrrr!"
# "Nothin'" otherwise

class pirate:

    def __init__(self):
        self.rums_drunk = 0
    
    def drink_rum(self):
        self.rums_drunk += 1

    def hows_goin_mate(self):
        if self.rums_drunk >= 5:
            return "Arrrr!"
        return "Nothin'"

Red_Earl = pirate()

# Megitatunk vele 4 rumot:
for i in range(1, 5):
    Red_Earl.drink_rum()

# 4 rum utuán megkérdezzük, mi a helyzet:
print(Red_Earl.hows_goin_mate()) # Nothin'

# Megitatunk vele egy 5. rumot:
Red_Earl.drink_rum()

# 5 rum utuán megkérdezzük, mi a helyzet:
print(Red_Earl.hows_goin_mate()) # "Arrrr!"
