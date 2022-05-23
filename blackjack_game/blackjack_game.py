'''
----------- CONTENTS -----------
'''
# 1. Object Classes
# 2. Functions
# 3. Default variables 


'''
----------- OBJECT CLASSES -----------
'''
# Card class
class Card:
    def __init__(self,suit,rank):
        #.title() methods used to avoid capitalization inconsistencies between args and reference lookups
        self.suit = suit.title()
        self.rank = rank.title()
        self.value = values[rank.title()]     
    def __str__(self):
        return self.rank + ' of ' + self.suit

# Deck Class
class Deck:
    '''
    when we instantiate Deck, create a list containing all 52 card objects 
    '''
    def __init__(self):
        self.all_cards = []
        # use nested loop w/ list-append to make each type of card in a deck
        for suit in suits:
            for rank in ranks:
                newcard = Card(suit,rank)
                self.all_cards.append(newcard)
    
    def __str__(self):
        complete = ''
        for card in self.all_cards:
            complete += ', ' + card.__str__()
        return f"The deck contains: {complete}"
        
    def __len__(self):
        return len(self.all_cards)
    
    def shuffle(self):
        random.shuffle(self.all_cards)
        
    def deal_one(self):
        return self.all_cards.pop()

        
# Player class
class Player:
    def __init__(self,name):
        self.name = name # could use name.lower() to avoid capitalization inconsistencies in their names
        
        self.all_cards = []
        self.score = 0
        self.bank = 0
        
    def __str__(self):
        return f'player {self.name} has {len(self.all_cards)} cards in deck'
    
    def add_cards(self,new_card):
        self.all_cards.append(new_card)
        #self.score += new_card.value
        
        self.score = self.score_check() # calls the score_check function to calculate score
        
    def reset_hand(self):
        self.all_cards = []
        self.score = 0
    
    def reset_bank(self):
        self.bank = 0
    
    def deposit(self,amt):
        self.bank += amt
    def withdraw(self,amt):
        self.bank -= amt
        
    ''' 
    # old version. removing 'score_alt' variable, pointless.
    def score_check(self):
        self.score_alt = 0
        aces = []
        other = []
        for card in self.all_cards:
            if card.rank == "Ace":
                aces.append(card)
            else:
                other.append(card)
        for card in other:
            self.score_alt += card.value
        for card in aces:
            if self.score_alt <= 10:
                self.score_alt += card.value
            else:
                self.score_alt += 1
        self.score = self.score_alt
        return self.score
        '''
    def score_check(self):
        #self.score_alt = 0
        self.score = 0
        aces = []
        other = []
        for card in self.all_cards:
            if card.rank == "Ace":
                aces.append(card)
            else:
                other.append(card)
        for card in other:
            self.score += card.value
        for card in aces:
            if self.score <= 10:
                self.score += card.value
            else:
                self.score += 1
        #self.score = self.score_alt
        return self.score
    
    def show_hand(self):
        complete = ''
        i = 0
        for card in self.all_cards:
            i += 1
            if i == 1:
                complete += card.__str__()
            else:
                complete += ', ' + card.__str__()
        return f"{complete}"
                

'''
----------- FUNCTIONS -----------
'''
def choose_bankroll():
    try:
        prompt_bank = int(input("default bankroll is 25 coins each. \tHit return to accept, or enter another number.\t"))
    except:
        bankroll = 25
    else:
        bankroll = prompt_bank
    finally:
        print(f"\t...using {bankroll} as bankroll\n")
        player.deposit(bankroll)
        dealer.deposit(bankroll)
        
def choose_bet():
    try:
        prompt_bet = int(input("\tDefault bet is 5 coins. \tHit return to accept, or enter another number.\t"))
    except:
        bet = 5
    else:
        bet = prompt_bet
    finally:
        print(f"\t...using {bet} as the wager.\n")
        player.withdraw(bet)
        dealer.withdraw(bet)
    return bet

def distribute_cards():
    for i in range(2):
        # Give 2 cards to dealer
        card_d = new_deck.deal_one()
        dealer.add_cards(card_d)
        
        # Give 2 cards to player
        card_p = new_deck.deal_one()
        player.add_cards(card_p)
        
        # ... show each player card:
        print(f"\t\tPlayer has received {card_p}. \tCurrent score = {player.score}")


def game_setup(mode='default',**kwargs):
    # instantiate players
    player = Player("player")
    dealer = Player("dealer")

    # instantiate card deck
    new_deck = Deck()
    new_deck.shuffle()

    #  pre-game var defaults
    game_on = True
    round_num = 0
    
    if mode == 'default':    
        return player,dealer,new_deck,game_on,round_num
        #elif mode == 'diag':
        #    return player,dealer,new_deck,game_on,round_num
    else:
        #for key,value in kwargs.items():
            #if type(key) = object, 
                #then apply key.value[0] as object.method, 
                # key.value[0](key.value[1]) as object.method(argument)
        game_on = False
        return player,dealer,new_deck,game_on,round_num

'''
----------- DEFAULTS -----------
'''

import random
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
        'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}


# Print Styles
h0 = ''
h1 = '\n\t'
h2 = '\n\t\t'
h3 = '\n\t\t\t'


#from blackjack_funcs_and_objectclasses import  Card,Deck,Player
#from blackjack_funcs_and_objectclasses import  choose_bankroll,choose_bet,distribute_cards,game_setup
''' 
# --- Pre-Game Setup ---
__________________________
'''
# instantiate players
player = Player("player")
dealer = Player("dealer")

# instantiate card deck
new_deck = Deck()
new_deck.shuffle()

#  pre-game var defaults
game_on = True
round_num = 0
'''
''' 
#def launch_game(mode='default',**kwargs):
    #player,dealer,new_deck,game_on,round_num = game_setup(mode='default',**kwargs)
'''
 ---- Start Game ----
________________________ 
'''

# ----- CHOOSE BANKROLL SIZE -----
choose_bankroll()

# ----- START SEQUENCE OF ROUNDS -----
while game_on: 
    ''' 
    # ---- Start Round ----
    _________________________
    '''
    # Reset Player cards and score
    player.reset_hand() 
    dealer.reset_hand()
    
    
    # Increase round number
    round_num += 1
    print(f"{h0}Starting Round #: {round_num}\n")
    
    print(f"{h2} Player bankroll: {player.bank}")
    print(f"{h2} Dealer bankroll: {dealer.bank}\n")
    
    # ----- CHOOSE BET SIZE -----
    bet = choose_bet()
    
    # ----- DISTRIBUTE CARDS ----
    distribute_cards()

    # ... show 1 dealer card 
    print(f"{h1}The Dealer hand contains a {dealer.all_cards[-1]}. \t Current score at least {dealer.all_cards[-1].value}")
    

    # ----- Begin turns -----
    ''' 
    # ---- Player & Dealer Turns ----
    _________________________________ 
    '''
    
    # player goes first:
    currentplayer = player 
    
    round_on = True
    while round_on:
        
        print(f"{h2}{currentplayer.name} hand: \t{currentplayer.show_hand()}{h3}\tscore \t= {currentplayer.score}")
        
        # --- prior to win, bust, or stay
        if currentplayer.score < 21: 
            while True:
                if currentplayer == player:
                    choice = input(f"{h2}Choose hit or stay. \t")
                    if choice.lower() == "hit" or choice.lower() == "stay":
                        break
                    else:
                        continue
                        
                elif currentplayer == dealer:
                    if dealer.score >= 17 or dealer.score > player.score:
                        choice = "stay"
                        break
                    else:
                        choice = "hit"
                        break
                else:
                    pass
            
            # --- Hit or Stay ---
            if choice == "hit":
                cardnew = new_deck.deal_one() 
                currentplayer.add_cards(cardnew)
                continue
                
            elif choice == "stay":
                if currentplayer == player:
                    currentplayer = dealer
                    print(f"{h1}Dealer turn begins.")
                    continue
                elif currentplayer == dealer:
                    if dealer.score > player.score:
                        print(f"{h1}dealer wins")
                        dealer.deposit(2*bet)
                    elif dealer.score == player.score:
                        print(f"{h1}this round is a tie!")
                        dealer.deposit(bet)
                        player.deposit(bet)
                    else:
                        print(f"{h1}player wins")
                        player.deposit(2*bet)
                        
                    round_on = False
                    break
            else:
                print("else. (unexpected)")
                pass
        
        # ---- if BLACKJACK ----
        elif currentplayer.score == 21:
            if currentplayer == player:
                print(f"{h1}player blackjack")
                currentplayer = dealer
                print(f"{h1}Dealer turn begins.")
                continue
            else:
                print(f"{h1}dealer blackjack")
                
                if player.score == 21 and dealer.score == 21:
                    print("round is a tie")
                    player.deposit(bet)
                    dealer.deposit(bet)
                    
                else:
                    print(f"{h1}dealer wins")
                    dealer.deposit(2*bet)
                    
                round_on = False
                break
        
        # ---- if BUST ----
        elif currentplayer.score > 21:
            print(f"{h1}BUST for {currentplayer.name}\n")
            
            if currentplayer == player:
                print(f"{h1}player busts \t\t ...dealer wins!")
                dealer.deposit(2*bet)
            else:
                print(f"{h1}dealer loses")
                player.deposit(2*bet)
                
            round_on = False
            break
        
        # ---- n/a ----
        else:
            print("else in round_on loop. UNexpected. breaking")
            game_on = False
            round_on = False
            pass
        
        # end manually
        test = input("DIAGNOSTIC PROMPT #1: \n\t press anything, or type 'quit' to quit:\n\t> ")
        if test == 'quit':
            game_on = False
            round_on = False
            break
    
    print(f"{h1}player score {player.score}, dealer score {dealer.score}")
    '''
    # Round over --- play again?
    ____________________________
    '''
    while round_on == False:
        if player.bank > 0 and dealer.bank > 0:
            playagain = input(f"{h0}play again? \t")
            if playagain.lower() == "y" or playagain.lower() == "yes":
                round_on = True
                continue
            else:
                print(f"{h1}Ending Game...")
                game_on = False
                break
        elif player.bank <= 0:
            print(f"{h1}player breaks the bank! \n\tGAME OVER")
            game_on = False
            break
        elif dealer.bank <= 0:
            print(f"{h1}dealer breaks the bank! \n\tGAME OVER")
            game_on = False
            break
        else:
            print("unexpected. \t ending game for diagnostics")
            game_on = False
            break
    
    '''
    #----------- Testing and Diagnostic Clauses -----------
    ___________________________________________________________
    '''
    # force quit prompt 
    test = input("DIAGNOSTIC PROMPT #2: \n\t press anything, or type 'quit' to quit:\n\t> ")
    if test == 'quit':
        game_on = False
        break
'''
if __name__ == '__main__':
    #mode = 'default'
    #launch_game(mode)

    #launch game
    launch_game()
else:
    pass
'''