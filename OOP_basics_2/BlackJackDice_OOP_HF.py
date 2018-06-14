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
My choice based the above instructions: Blackjack Dice Game 

Rules of the game (source: http://www.netexl.com/howtoplay/blackjack-dice/):

Blackjack Dice is the dice version of popular card game Blackjack and has a
 similar objective of getting closest to 21 without going over. The game is
 played with 2 six-sided dice.

Blackjack Dice Game Play:
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
"""

import random


class Player(object):
    
    def __init__(self, name):
        self.name = name
        self.turn_total = 0
        self.points = 0
        self.dice_number = 0
    
    def roll(self):
        self.dice_number = random.randrange(1, 6, 1)
        self.turn_total += self.dice_number
        return self.dice_number

    def newturn(self):
        self.turn_total = 0
        self.dice_number = 0
        

#def BlackJackDice(players, max_points):

    #@@ 1. while ciklus: addig mennek a játék-körök, amíg valamelyik játékos el nem éri a megadott limit-pontszámot (pl. 10 pont)
        #@@ 2. while ciklus: addig megy egy kör, amíg valaki el nem éri/meg nem haladja a 21-et, vagy amíg mindenki meg nem áll

print('@@IDE JÖN MAJD A JÁTÉKSZABÁLY')
print('\r\n')

players = []

num_of_players = 0
print('Gépeld be a játékosok számát (legalább 2, legfeljebb 6), majd nyomj Entert!')
while num_of_players not in range(2, 7, 1):
    try:
        num_of_players = int(input())
        if num_of_players not in range(2, 7, 1):
            print('2 és 6 közötti egész számot kell megadni!')
    except ValueError:
        print('2 és 6 közötti egész számot kell megadni!')

for i in range(0, num_of_players):
    print('Gépeld be a(z) ' + str(i + 1) + '. játékos nevét, majd nyomj Entert!')
    players.append(Player(input())) 

max_points = 0
print('Gépeld be, hogy hány pontig szeretnétek játszani (legalább 10, legfeljebb 30), majd nyomj Entert!')
while max_points not in range(10, 30, 1):
    try:
        max_points = int(input())
        if max_points not in range(10, 30, 1):
            print('10 és 30 közötti egész számot kell megadni!')
    except ValueError:
        print('10 és 30 közötti egész számot kell megadni!')
