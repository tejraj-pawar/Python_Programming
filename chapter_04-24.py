'''
(Game: pick a card ) Write a program that simulates picking a card from a deck of
52 cards. Your program should display the rank (Ace, 2, 3, 4, 5, 6, 7, 8, 9, 10,
Jack, Queen, King) and suit (Clubs, Diamonds, Hearts, Spades) of the card.
Here is a sample run of the program:

The card you picked is the Jack of Hearts
'''
import random

rank = random.randint(1, 13)
suit = random.randint(1, 4)

print('The card you picked is the', end=' ')

if rank == 1:
    print('Ace', end=' ')
elif rank == 2:
    print(rank, end=' ')
elif rank == 3:
    print(rank, end=' ')
elif rank == 4:
    print(rank, end=' ')
elif rank == 5:
    print(rank, end=' ')
elif rank == 6:
    print(rank, end=' ')
elif rank == 7:
    print(rank, end=' ')
elif rank == 8:
    print(rank, end=' ')
elif rank == 9:
    print(rank, end=' ')
elif rank == 10:
    print(rank, end=' ')
elif rank == 11:
    print("Jack", end=' ')
elif rank == 12:
    print("Queen", end=' ')
elif rank == 13:
    print("King", end=' ')

print("of", end=' ')

# Clubs, Diamonds, Hearts, Spades
if suit == 1:
    print('Clubs')
elif suit == 2:
    print('Diamonds')
elif suit == 3:
    print('Hearts')
elif suit == 4:
    print('Spades')
