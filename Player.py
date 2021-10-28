from Hand import Hand

class Player(Hand):   
    hand = []

    def __init__(self): 
        super().__init__(self.hand)

    def __str__(self):
        result = "Player Hand: "
        for card in self.hand: 
            result += card + " "
        result += "\nTotal: " + str(self.hand_value)
        return result
