# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

import simplegui

def name_to_number(name):
    # convert name to number
    if name == 'rock':
        return 0
    elif name == 'Spock':
        return 1
    elif name == 'paper':
        return 2
    elif name == 'lizard':
        return 3
    elif name == 'scissors':
        return 4
    else:
        return -1

def number_to_name(number):
    # convert number to a name 
    # convert name to number
    if number == 0:
        return 'rock'
    elif number == 1:
        return 'Spock'
    elif number == 2:
        return 'paper'
    elif number == 3:
        return 'lizard'
    elif number == 4:
        return 'scissors'
    
import random

computer_number = 0

def compChoice():
    global computer_number
    computer_number = random.randrange(0,5)

def rpsls(player_choice): 
    print 
    player_number = name_to_number(player_choice)
    print 'Player chooses', player_choice
    computer_number
    computer_choice = number_to_name(computer_number)
    print 'Computer chooses', computer_choice
    difference = computer_number - player_number
    if player_number == -1:
        print "Player entered an invalid choice.. Try again."
    else:
        if player_choice == computer_choice:
            print 'Player and computer tie!'
        elif difference % 5 <= 2:
            print 'Computer wins!'
        else:
            print 'Player wins'
    
frame = simplegui.create_frame('rpsls', 300, 300)
frame.add_button('computer choice', compChoice, 100)
inp = frame.add_input('Enter your choice :', 	rpsls, 100)
inp.set_text('result')
frame.start()
'''
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
'''