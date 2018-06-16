"""\
HOMEWORK

1) Check out this page: http://knightlab.northwestern.edu/2014/06/05/five-mini-programming-projects-for-the-python-beginner/
2) Pick a game that you like the most
3) Build it with Classes in mind

Focus on:
- Modularization
- Encapsulation
- Code reusability
"""

"""\
1. Dice Rolling Simulator

The Goal: Like the title suggests, this project involves writing a program that
 simulates rolling dice. When the program runs, it will randomly choose a number
 between 1 and 6. (Or whatever other integer you prefer — the number of sides on
 the die is up to you.) The program will print what that number is. It should
 then ask you if you’d like to roll again. For this project, you’ll need to set
 the min and max number that your dice can produce. For the average die, that
 means a minimum of 1 and a maximum of 6. You’ll also want a function that
 randomly grabs a number within that range and prints it.
 
Concepts to keep in mind:
 - Random
 - Integer
 - Print
 - While Loops


A good project for beginners, this project will help establish a solid
 foundation for basic concepts. And if you already have programming
 experience, chances are that the concepts used in this project aren’t
 completely foreign to you. Print, for example, is similar to Javascript’s
 console.log.
"""

"""\
My choice based on the above instructions:
_________________________________________________________________________________

Blackjack Dice Game 
_________________________________________________________________________________
"""

import random


class Player(object):
    
    def __init__(self, name):
        self.name = name
        self.turn_total = 0
        self.points = 0
        self.dice_number = 0
        self.stopped = False
    
    def roll(self):
        self.dice_number  = random.randrange(1, 6, 1)
        self.turn_total  += self.dice_number
        return self.dice_number

    def new_round(self):
        self.turn_total = 0
        self.dice_number = 0

    def stop(self):
        self.stopped = True
        

def BlackJackDice(players, max_points):            

    players_points = {}
    
    somebody_won = False

    which_round = 0
    
    while not somebody_won: #@@ 1. while ciklus: addig mennek a játék-körök, amíg valamelyik játékos el nem éri a megadott limit-pontszámot (pl. 10 pont)
        which_round += 1
        somebody_is_over_21 = False
        for i in players:
            i.new_round()
        print('\n________________________________________________________________________________\n')
        print('Round ' + str(which_round))
        print('________________________________________________________________________________\n')
        
        while not somebody_is_over_21: #@@ 2. while ciklus: addig megy egy kör, amíg valaki el nem éri/meg nem haladja a 21-et, vagy amíg mindenki meg nem áll
            for i in players:
                if not i.stopped:
                    print(i.name + ', press Enter to roll!')
                    EnterPressed = input()
                    roll_1_result = i.roll()
                    roll_2_result = i.roll()
                    print(str(roll_1_result) + '    ' + str(roll_2_result))
                    print('Turn total of ' + i.name + ': ' + str(i.turn_total))
                    print('\n')
                    somebody_is_over_21 = i.turn_total >= 21

        print('\nEND OF ROUND ' + str(which_round) + '\n')    

        
        for i in players:
            players_points[i.name] = i.points
            if i.points >= max_points:
                somebody_won = True

        print('Scores at the end of round ' + str(which_round) + ':')
        for i in players_points.keys():
            print('    ' + i + ': ' +  str(players_points[i]))
    
print("""
________________________________________________________________________________

                           LET'S PLAY BLACKJACK DICE!

                ________             __________
              |\ *    *  \          /*        /|
              | \ *    *  \        /    *    / |
              |* \_*____*__\      /________*/  |
              |  |         |     |         |   |
              |  |  *    * |     |  *      | * |
              \ *|         |     |         |  /
               \ |  *    * |     |       * | /
                \|_________|     |_________|/

________________________________________________________________________________
"""
)
print('\n')
print("""
RULES OF THE GAME:
(source: http://www.netexl.com/howtoplay/blackjack-dice/)

INTRODUCTION:
 Blackjack Dice is the dice version of popular card game Blackjack and has a
 similar objective of getting closest to 21 without going over. The game is
 played with 2 six-sided dice.

BLACKJACK DICE GAMEPLAY::
 Players take turn clockwise to roll dice and score as per the following rules

 In each turn players roll two dice and add the numbers to their turn total.
 Players can roll as many times as they wish.
 Once players have scored 16 or more, they have the option to stop rolling or
 just roll one die one or more times.
 If their score goes over 21, then they bust and their turn score is zero.
 The aim is to score 21 or get closest to 21 without going over.
 Each player scoring 21 in the round gets 2 points.
 If no player scores 21 then the player closest to 21 gets 1 point. If more
 than one player have the same score, then no point is given to any player.
 The game is played for multiple rounds and the first player to reach to a
 predetermined score (for ex 10 or 20 points) wins the game.
""")
print('\n')

players = []

num_of_players = 0
print('Type the number of players (at least 2, up to 6) then press Enter!')
while num_of_players not in range(2, 7, 1):
    try:
        num_of_players = int(input())
        if num_of_players not in range(2, 7, 1):
            print('Number of players must be an integer between 2 and 6!')
    except ValueError:
        print('Number of players must be an integer between 2 and 6!')

for i in range(0, num_of_players):
    if i + 1 == 1:
        th = 'st'
    elif i + 1 == 2:
        th = 'nd'
    elif i + 1 == 3:
        th = 'rd'
    else:
        th = 'th'
    print('Type the name of the ' + str(i + 1) + th + ' player then press Enter!')
    players.append(Player(input())) # @@ Itt valahogy tiltani kéne, hogy "" legyen a neve!

max_points = 0
print('Type the score you want to reach (at least 10, up to 30) then press Enter! Whichever player first reaches this score wins the game.')
while max_points not in range(10, 31, 1):
    try:
        max_points = int(input())
        if max_points not in range(10, 31, 1):
            print('The predetermined score must be an integer between 10 and 30!')
    except ValueError:
        print('The predetermined score must be an integer between 10 and 30!')

BlackJackDice(players, max_points)
