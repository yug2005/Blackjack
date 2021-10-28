from Player import Player
from Dealer import Dealer

print("Welcome to Blackjack!")

while True: 
    try:
        knows_blackjack = str(input("Do you know how to play blackjack? (yes/no) ")).lower()
    except ValueError:
        print("Invalid Input. Please enter a string.")
        continue
    
    if (knows_blackjack == "yes"):
        break
    elif (knows_blackjack == "no"):
        instructions = open("instructions.txt", "r")
        print(instructions.read())
        instructions.close()
        input("Press enter to continue ")
        break
    else: 
        print("Please enter yes or no.")

current_balance = 1000
game_over = False
def print_balance(balance):
    print("Your current balance is " + str(balance) + ".")

while (not game_over): 
    print_balance(current_balance)
    while True:
        try:
            bet = int(input("Place a bet: "))
            if (bet <= current_balance): 
                break
            else:
                print("You do not have enought to place this bet.")
        except ValueError:
            print("Please enter a number.")

    player = Player()
    dealer = Dealer()
    print(player)
    print(dealer)

    while True: 
        try: 
            hit_or_stand = input("Do you want to hit or stand? ").lower()
            if (hit_or_stand == "hit"):
                player.add_card()
                print(player)
                if (player.hand_value > 21):
                    break
                continue
            elif (hit_or_stand == "stand"): 
                while (dealer.hand_value < 17):
                    print("Dealer hits.")
                    dealer.add_card()
                    print(dealer)
                    if (dealer.hand_value > 21): 
                        break
                    input("Press enter to continue ")
                print("Dealer stands.")
                break 
            else: 
                print("Please enter hit or stand")
        except ValueError:
            print("Invalid Input.")

    if (player.hand_value == dealer.hand_value): 
        print("You push.")
    elif (player.hand_value == 21):
        print("Blackjack! You win!")
        current_balance += 3.0 * bet / 2.0
    elif (player.hand_value > 21): 
        print("You busted. Dealer wins.")
        current_balance -= bet
    elif (dealer.hand_value > 21): 
        print("Dealer busted. You win!")
        current_balance += bet  
    elif (player.hand_value > dealer.hand_value): 
        print("You win!")
        current_balance += bet
    else: 
        print("Dealer wins.")
        current_balance -= bet

    print_balance(current_balance)
    
    player.clear_hand()
    dealer.clear_hand()

    if (current_balance > 0):
        while True:
            try:
                play_again = input("Do you want to play again? (yes/no) ")
                if (play_again == "yes"):
                    break
                elif (play_again == "no"):
                    print("Thanks for playing. I hope you have a wonderful day.")
                    game_over = True
                    break
                else:
                    print("Please enter yes or no.")
            except ValueError:
                print("Invalid Input")
    else: 
        print("Your balance is 0. Thanks for playing. I hope you have a wonderful day.")
        game_over = True