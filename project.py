# Make a game of 3-card poker that the player can play against the AI.
import random
import sys

# Create a Hand class for the dealer and the player
class Hand:
    def __init__(self,cards):
        self.cards = cards
        self.value = 0
        self.card1,self.card2,self.card3 = Hand.card_values(self)

    # Check if hand is Straight, Flush, 3 of a kind or pair. Value each hand for comparision with an int.
    # Straight Flush = 6000000  Three = 5000000  Straight = 4000000  Flush = 3000000  Pair = 2000000   High = 1000000
    # All values have 6 empty zeros to also compare the values of the cards. A=14,K=13,Q=12,J=11 
    # Ex. Flush with ace, 5 and 3 should equal 3140503 which would win against a flush with ace,5,and 4 which would equal 3140504
    def value_hand(self):
        self.value =0
        if self.check_flush() and self.check_straight():
            self.value += 6000000
        elif self.check_three():
            self.value +=5000000
        elif self.check_straight():
            self.value += 4000000
        elif self.check_flush():
            self.value += 3000000
        elif self.check_pair():
            self.value += 2000000
        else:
            self.value +=1000000
        
        if self.card1>= self.card2 and self.card1>= self.card3:
            self.value += self.card1*10000
            if self.card2>=self.card3:
                self.value += self.card2*100
                self.value += self.card3
            else:
                self.value += self.card3*100
                self.value += self.card2
        elif self.card2>= self.card3 and self.card2 >= self.card1:
            self.value += self.card2*10000
            if self.card1>=self.card3:
                self.value += self.card1*100
                self.value += self.card3
            else:
                self.value += self.card3*100
                self.value += self.card1
        else:
            self.value += self.card3*10000
            if self.card1>=self.card2:
                self.value += self.card1*100
                self.value += self.card2
            else:
                self.value += self.card2*100
                self.value += self.card1
        return self.value
        

    def __str__(self):
        return f" hand: {self.cards[0]}, {self.cards[1]}, and {self.cards[2]}."
    
    @property
    def cards(self):
        return self._cards
    
    @cards.setter
    def cards(self, cards):
        self._cards = cards

    # Check if the suit letters are equal, return True if they are.
    def check_flush(self):
        if self.cards[0][len(self.cards[0])-1] == self.cards[1][len(self.cards[1])-1] and self.cards[0][len(self.cards[0])-1] == self.cards[2][len(self.cards[2])-1]:
            return True
        else:
            return False

    # Find the lowest card value and add 1. If either other card is equal go forth and check the last card.
    def check_straight(self):
        if self.card1 < self.card2 and self.card1 < self.card3:
            if self.card2 == self.card1+1:
                if self.card3 == self.card1+2:
                    return True
            elif self.card3 == self.card1+1:
                if self.card2 == self.card1+2:
                    return True
        elif self.card2 < self.card3:
            if self.card1 == self.card2+1:
                if self.card3 == self.card2+2:
                    return True
            elif self.card3 == self.card2+1:
                if self.card1 == self.card2+2:
                    return True
        else:
            if self.card2 == self.card3+1:
                if self.card3 == self.card3+2:
                    return True
            elif self.card1 == self.card3+1:
                if self.card2 == self.card3+2:
                    return True


    # See if the value of each card are equal to eachother
    def check_three(self):
        if self.card1 == self.card2 and self.card1 == self.card3:
            return True
        else:
            return False

    # See if the value of two cards are equal to eachother
    def check_pair(self):
        if self.card1 == self.card2 or self.card1 == self.card3 or self.card2 == self.card3:
            return True
        else:
            return False

    # Returns the numeric values of all the cards.
    def card_values(self):
        for i in range(3):
            match self.cards[i-0][0]:
                case 'A':
                    exec(f'self.card{i+1} =int(14)')
                case 'K':
                    exec(f'self.card{i+1} =int(13)')
                case 'Q':
                    exec(f'self.card{i+1} =(12)')
                case 'J':
                    exec(f'self.card{i+1} =(11)')
                case '1':
                    exec(f'self.card{i+1} =(10)')
                case other:
                    exec(f'self.card{i+1} =int(self.cards[i][0])')
        return self.card1,self.card2,self.card3
                    


# Reinitialize the deck
def shuffle():
    deck = ['AH','2H','3H','4H','5H','6H','7H','8H','9H','10H','JH','QH','KH',
            'AD','2D','3D','4D','5D','6D','7D','8D','9D','10D','JD','QD','KD',
            'AS','2S','3S','4S','5S','6S','7S','8S','9S','10S','JS','QS','KS',
            'AC','2C','3C','4C','5C','6C','7C','8C','9C','10C','JC','QC','KC',]
    return deck

# Return 3 cards from the deck and removes them when they are chosen.
def deal_3(deck):
    hand = []
    for i in range(3):
        index = random.randint(0,len(deck)-1-i)
        hand.append(deck[index])
        deck.remove(deck[index])
    return hand, deck

def display_rules():
    print("\nWelcome to Three Card Poker \n"
          "Your goal is to get a higher poker hand than the dealer. \n"
          "The dealer plays on a queen high or higher.\n"
          "You have to bet a play bet and an optional pair plus bet before the cards are dealt. \n"
          "In order to play your hand you must double your play bet with an ante bet after getting your cards. \n"
          "For hand information enter 1. For betting payouts enter 2. To check your balance enter 3. To display rules again, enter 4. \n"
          "To play enter 0. To stop playing enter 5. \n \n")
    
def display_hands():
    print("\n \n Hands ranked highest to lowest: \n"
          "Straight Flush: A hand that has three cards in the same suit and consecuative ranking.\n"
          "Three of a Kind: A hand that has three cards of the same rank.\n"
          "Straight: A hand that consists of three cards in consecutive ranking.\n"
          "Flush: A hand that consists of three cards of the same suit. \n"
          "One pair: A hand that consists of two cards of the same rank. \n"
          "High card: A hand that consists of three cards not matching the hands above, so it is ranked by the highest ranked card. \n \n")

def display_betting():
    print("\n \n Play bet Payouts: \n"
          "By beating the dealers hand your play bet is payed out 1:1 \n"
          "If the dealer doesn't have a queen high to play, your play bet is returned to you. \n"
          "\n Ante bet Payouts: \n"
          "By beating the dealers hand your ante bet is payed out 1:1 \n"
          "If the dealer doesn't have a queen high to play, your ante bet is still payed out 1:1 \n"
          "If you have a straight your ante bet gets a bonus payout of 1:1 \n"
          "If you have a three of a kind your ante bet gets a bonus payout of 4:1 \n"
          "If you have a Straight flush your ante bet gets a bonus payout of 5:1 \n"
          "\n Pair Plus Payouts: \n"
          "Pair plus only pays for special hands, there's no base payout for winning or losing the hand. \n"
          "A pair grants the payout of 1:1 \n"
          "A flush grants the payout of 4:1 \n"
          "A Straight grants the payout of 6:1 \n"
          "A Three of a kind grants the payout of 30:1 \n"
          "A Straight Flush grants the payout of 40:1 \n \n"
          "This table's betting limits is $5000 for play bets and $1000 for pair plus bets. Only whole numbers are accepted. \n \n")

def display_balance(balance):
    print(f'You have a balance of ${float(balance):,.2f} \n \n')

def end_program(balance):
    print(f'You have a final balance of ${float(balance):,.2f} \n \n'
          'Thanks for playing')
    sys.exit()
    
def check_choice(input, balance):
    match input:
        case "1":
            display_hands()
        case "2":
            display_betting()
        case "3":
            display_balance(balance)
        case "4":
            display_rules()
        case "0":
            balance = play_round(balance)
            return balance
        case "5":
            end_program(balance)


# Prompt user for an int bet, check if the bet is <= to balance/s and >0 and <5000. Then get pair plus bet if it's >0,<1000
def get_bet(balance):
    while True:
        temp_balance = balance
        try:
            play = int(input("What is your play bet? "))
            if play <= temp_balance/2 and play <= 5000 and play >=0:
                temp_balance -= play*2
            else:
                print(f"Your play bet has to be at more than $0, Less than $5000 and less than half your balance of ${balance:,.2f}")
                raise ValueError
            pair = int(input("What is your pair plus bet? "))
            if pair <=temp_balance and pair <=1000 and pair >=0:
                temp_balance -= pair
                break
            else:
                print(f"Your pair plus bet has to be at least $0, Less than $1000 and less than your balance of ${temp_balance:,.2f} after the play bet.")
                raise ValueError
        except ValueError or TypeError:
            continue
    balance -= play
    balance -= pair

    return play,pair,balance

def check_bonus(play, pair, player):
    if player.value_hand() >=6000000:
        return pair*41 + play*6
    elif player.value_hand() >=5000000:
        return pair*31 + play*5
    elif player.value_hand() >=4000000:
        return pair*7 + play*2
    elif player.value_hand() >=3000000:
        return pair*5
    elif player.value_hand() >=2000000:
        return pair*2
    else:
        return 0
    

def get_payout(play, pair, balance, player, dealer):
    # If dealer Plays
    if dealer.value_hand() >= 1120000:
        if player.value_hand() > dealer.value_hand():
            print("You beat the dealer's " + str(dealer))
            balance += play*4 + check_bonus(play, pair, player)
        elif player.value_hand() == dealer.value_hand():
            print("You pushed the dealer's " + str(dealer))
            balance += play*2 + check_bonus(play, pair, player)
        elif player.value_hand()< dealer.value_hand():
            print("You lost to the dealer's " + str(dealer))
            balance += check_bonus(play, pair, player)
    elif dealer.value_hand() < 1120000:
        if player.value_hand() > dealer.value_hand():
            print("You beat the dealer's " + str(dealer) + " But the dealer didn't play.")
            balance += play*3 + check_bonus(play, pair, player)
        elif player.value_hand() == dealer.value_hand():
            print("You pushed the dealer's " + str(dealer) + " But the dealer didn't play.")
            balance+= play*3 + check_bonus(play, pair, player)
        elif player.value_hand()< dealer.value_hand():
            print("You lost to the dealer's " + str(dealer) + " But the dealer didn't play.")
            balance += play*3 + check_bonus(play, pair, player)
    return balance

def play_round(balance):
    deck = shuffle()
    cards,deck = deal_3(deck)
    play,pair,balance = get_bet(balance)
    player = Hand(cards)
    cards,deck = deal_3(deck)
    dealer = Hand(cards)
    print("Your" + str(player))
    while True:
        fold = input("Do you want to play this hand? (Y/N) ").strip().lower()
        if fold =='y':
            balance -= play
            balance = get_payout(play, pair, balance, player, dealer)
            break
        elif fold == 'n':
            break
    return balance


def main():
    display_rules()
    balance = 10000
    while True:
        print("\n")
        choice = input("Enter your choice: ")
        print("\n")
        if choice == "0":
            balance = check_choice(choice, balance)
        else:
            check_choice(choice, balance)
        if balance == 0:
            end_program(balance)

if __name__ == "__main__":
    main()
    