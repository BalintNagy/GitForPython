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
        self.one_die_only = False
        self.stopped = False
    
    def roll(self):
        dice_number_rolled  = random.randrange(1, 6, 1)
        self.turn_total  += dice_number_rolled
        return dice_number_rolled
    
    def roll_with_two_dice(self):
        roll_1_result = self.roll()
        roll_2_result = self.roll()
        print(str(roll_1_result) + '    ' + str(roll_2_result))
    
    def roll_with_one_die(self):
        roll_1_result = self.roll()
        print(str(roll_1_result))
    
    def new_round(self):
        self.turn_total = 0
        self.one_die_only = False
        self.stopped = False
    
    def one_die(self):
        self.one_die_only = True
    
    def stop(self):
        self.stopped = True
    
    def bust(self):
        self.stop()
        print(self.name + ' busted.\n')
    
    def reached_21(self):
        print(self.name + ' reached 21 in this round and gets 2 points!\n')
        self.points += 2
        self.stop()        

def intro():
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
 predetermined score (for ex 10 or 20 points) wins the game.\n
    """)

    print('GAME SETTINGS\n')

def set_players():
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

    return players
    

def set_max_points():
    max_points = 0
    print('Type the score you want to reach (at least 5, up to 30) then press Enter! Whichever player first reaches this score wins the game.')
    while max_points not in range(5, 31, 1):
        try:
            max_points = int(input())
            if max_points not in range(5, 31, 1):
                print('The predetermined score must be an integer between 5 and 30!')
        except ValueError:
            print('The predetermined score must be an integer between 5 and 30!')
    return max_points

def BlackJackDice(players, max_points):            
    
    players_points = {}
    somebody_won = False
    which_round = 0
    
    while not somebody_won:
        which_round += 1
        turn_is_over = False
        for i in players:
            i.new_round()
        print('\n________________________________________________________________________________\n')
        print('Round ' + str(which_round))
        print('________________________________________________________________________________\n')
        
        while not turn_is_over:
            we_have_a_winner = False
            for i in players:
                if not i.stopped:
                    if i.turn_total >= 16:
                        print(i.name + ', your turn total is now ' + str(i.turn_total) + '.')
                        print('If you want to stop rolling type "s".')
                        print('If you want to continue rolling with one die only type "1".')
                        possible_answers = ['s', '1']
                        possible_answers_str = '"s" or "1"'
                        if not i.one_die_only:
                            print('If you want to continue rolling with two dice type "2".')
                            possible_answers.append('2')
                            possible_answers_str = '"s", "1" or "2"'
                        answer = ''
                        while answer not in possible_answers:
                            print('Type your answer (' + possible_answers_str + ') then press Enter!')
                            answer = input()
                        if answer == 's':
                            i.stop()
                        elif answer == '1':
                            i.one_die()
                    if not i.stopped: 
                        print(i.name + ', press Enter to roll!')
                        EnterPressed = input()
                        if not i.one_die_only:
                            i.roll_with_two_dice()
                        else:
                            i.roll_with_one_die()
                    print('Turn total of ' + i.name + ': ' + str(i.turn_total) + '\n')
                    
                    if i.turn_total == 21:
                        i.reached_21()
                        we_have_a_winner = True
                    
                    if i.turn_total > 21:
                        i.bust()
                        
            number_of_stopped_players = 0
            number_of_busted_players = 0
            for i in players:
                if i.stopped:
                    number_of_stopped_players += 1
                if i.turn_total > 21:
                    number_of_busted_players += 1
            
            turn_is_over = number_of_stopped_players == len(players) or we_have_a_winner or number_of_busted_players == len(players) - 1 
            if turn_is_over and not we_have_a_winner:
                winner_of_the_turn = ''
                max_turn_total = 0
                tie = False
                for player in players:
                    if player.turn_total < 21 and player.turn_total > max_turn_total:
                        max_turn_total = player.turn_total
                        winner_of_the_turn = player
                    elif player.turn_total == max_turn_total: #ha holtverseny van
                        tie = True
                        break
                if winner_of_the_turn == '' or tie:
                    if tie:
                        print("It's a tie. Nobody gets point in this round.")
                    else:
                        print('Nobody gets point in this round.')
                else:
                    if not tie:
                        winner_of_the_turn.points += 1
                        print(winner_of_the_turn.name + ' got closest to 21 thus gets 1 point!')
                    
                
        
        print('\nEND OF ROUND ' + str(which_round) + '\n')    
        
        
        winner_of_the_game = ''
        for player in players:
            players_points[player.name] = player.points
            if player.points >= max_points:
                winner_of_the_game = player
                somebody_won = True
        
        print('Scores at the end of round ' + str(which_round) + ':')
        for i in players_points.keys():
            print('    ' + i + ': ' +  str(players_points[i]))

    print('\nEND OF GAME\n')
    print(winner_of_the_game.name + ' won the game!')
            
intro()
BlackJackDice(set_players(), set_max_points())
