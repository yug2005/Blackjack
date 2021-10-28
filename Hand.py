import random

class Hand: 
    used_cards = []
    hand_value = 0

    cards_file = open("cards.txt", "r")
    cards = cards_file.read().splitlines()
    cards_file.close()

    def __init__(self, hand):
        self.hand = hand
        self.add_card()
        self.add_card()

    def add_card(self): 
        while True: 
            card_index = random.randint(0, 51)
            if card_index not in self.used_cards: 
                card = self.cards[card_index]
                self.hand.append(card)
                self.hand_value += self.get_card_value(card)
                self.used_cards.append(card_index)
                break

    def get_card_value(self, card):
        if (card[0] == 'A'):
            # if the hand can afford it, the value is 11 and if not the value is 1
            if (self.hand_value <= 10):
                return 11 
            else:
                return 1
        elif (card[0] == 'J' or card[0] == 'Q' or card[0] == 'K' or card[0] == '1'):
            return 10
        else:
            return int(card[0])

    def clear_hand(self):
        self.hand = []


