# Rock-Paper-Scissors
# Rock-Paper-Scissors is a simple two-player game where, at a signal,
# players make figures with their hands, representing a rock, a piece of paper,
# or a  pair of scissors. The winner is determined according to a set of rules.
# You can find the official rules under the Resources.

# "R" for "rock",
# "P" for "paper",
# "S" for "scissors".
import random

myShape = ['P', 'R', 'S']
player = cpu = validEntry = None
while player == cpu or validEntry == 'No':
    player = input('Enter your choice [R, P or S]: ')
    player = player.capitalize()
    cpu = random.choice(myShape)
    if player == cpu:
        print('Draw! Try again')
        print('player(' + player + ') and CPU(' + cpu + ')')
    elif player == 'P' or player == 'R' or player == 'S':
        if player == 'P' and cpu == 'R':
            print('Player(Paper):CPU(Rock)')
            print('Game Over!')
            print('Player Won')
        elif player == 'R' and cpu == 'P':
            print('Player(Rock):CPU(Paper)')
            print('Game Over!')
            print('CPU Won')
        elif player == 'P' and cpu == 'S':
            print('Player(Paper):CPU(Scissors)')
            print('Game Over!')
            print('CPU Won')
        elif player == 'S' and cpu == 'P':
            print('Player(Scissors):CPU(Paper)')
            print('Game Over!')
            print('Player Won')
        elif player == 'S' and cpu == 'R':
            print('Player(Scissors):CPU(Rock)')
            print('Game Over!')
            print('CPU Won')
        else:
            print('Player(Rock):CPU(Scissors)')
            print('Game Over!')
            print('Player Won')
        validEntry = 'Yes'
    else:
        print('Your entry was invalid')
        validEntry = 'No'
