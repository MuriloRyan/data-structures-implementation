#it uses stacks (/src/stacks.py)
from src.stacks import Stack
import random

card_suits = ('hearts', 'diamonds', 'clubs', 'spades')
card_ranks = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']

class Card:
    def __init__(self, card_data=None):
        self.data = card_data
    
    def __repr__(self):
        return str(self.data)

def _generate_deck(stack_class=Stack,card_class=Card):
    deck = Stack()
    for suit in card_suits:
        for rank in card_ranks:
            deck.push(Card(card_data={'suit': suit, 'rank': rank}))

    return deck

def _shuffle_deck(deck: Stack):
    deck_list = []

    for card in deck:
        deck_list.append(card)
    
    random.shuffle(deck_list)

    shuffled_deck = Stack()
    for card in deck_list:
        shuffled_deck.push(card)

    return shuffled_deck

def create_deck(generate_function=_generate_deck,shuffle_function=_shuffle_deck):
    deck = generate_function()
    deck = shuffle_function(deck)

    return deck


def main(deck=None):
    deck = create_deck() if not deck else deck

    command = input('\nInsert your command: ')

    if command.lower() in ('pull card', 'pull', 'peak'):

        print('\nyour card is:', deck.pop())
        print()

        return main()
    
    elif command.lower() in ('length', 'len'):

        print('\nthe deck length is: ', len(deck))

        return main()
    
    elif command.lower() in ('exit', 'stop', 'quit'):
        return 0

    else:

        print("\nwrong command!\nYou can type 'exit' or 'quit' for stop the code")

        return main()

main()