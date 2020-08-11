#Importing Needed Modules
from random import choice as rand   #RNG Function
from os import system as sys        #To clear the screen after certain calls

#Defining Programs
def play_blackjack():
    #Cache flushed each round:
    rngroll = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,5]
        
    hand = [0]             #your hand; [0] is value and [1:] are the cards
    aceCount = [0]             #number of ace cards
    cache = [
        ["|¯¯¯¯¯¯˥"],   #0
        [],             #1 Identifier
        [],             #2 Suit
        [],             #3 Suit
        [],             #4 Identifier
        ["|______˩"],   #5
    ]
    
    def scorecheck():
        if stage[0] > max_stage[0]:
            sys('cls')
            print("You've completed your last round. Final score: " + str(score[0]) + "\nGoodbye!")
            exit()

        else:
            sys('cls')
            print("\nRound " + str(stage)[1:-1] + " of " + str(max_stage)[1:-1])
            print("Total Score: " + str(score[0]) + "\n")
            print("\nYour Hand (" + str(hand[0]) + "/21): " + ", ".join(hand[1:]))
            if hand[0] > 1:
                print("Last Card Drawn:")
                for line in cache:
                    print("".join(line))
    
        while True:
            try:
                card = int(input("Draw Card? 1 for yes or 2 to end the round "))
            except ValueError:
                sys('cls')
                print("Bad Value. Try Again.")
            if card == int(1):
                drawcard()
            elif card == int(2):
                eor_scoring()
    
    def drawcard():
        #chooses a random number 1-52; based off of the rngroll table
        x = rand(rngroll)        
        
        #removes possibility that same card can be referenced twice in one round
        rngroll.remove(x)

        #adds the name of the card to the player's hand
        hand.append(deck[x-1][1])
        
        #Adds numerical value to the player's hand[0]
        hand[0] += int(deck[x-1][2])

        #If you go over 21, checks to see if you have an ace
        if 'Ace' in deck[x-1][1]:
            aceCount[0] += 1
        
        visual_cards()
        scorecheck()
    
    def eor_scoring():
        #Tallys game score, returns to scorecheck (resets rng table and hand)
        if hand[0] < 21:
            score[0] += 3*(21-hand[0])
        elif hand[0] == 21:
            score[0] += 0
        elif hand[0] > 21:
            score[0] += 7 * (hand[0]-21)
        stage[0] += 1
        play_blackjack()

    def visual_cards():
        print(hand)
        for x in deck:
            if x[1] in hand[-1:]:
                if '10 of ' in x[1]:
                    cache[1] = "|10    |"
                    cache[4] = "|    10|"

                else:
                    cache[1] = str("|" + x[3] + "     |")
                    cache[4] = str("|     " + x[3] + "|")
            
                cache[2] = str("|" + x[4] + "     |")
                cache[3] = str("|     " + x[4] + "|")    

        for y in cache:
            print("".join(y))
            
    scorecheck()

def NumberOfRounds():
    while True:
        try:
            max_stage[0] = int(input("Select number of rounds: "))
        except ValueError:
            sys('cls')
            print("Bad Value. Try Again.")
        if max_stage[0] < 1:
            sys('cls')
            print("Bad Value. Try Again.")
        else:
            play_blackjack()

#Static Variables; are not flushed after each round
deck = [
    #0      1                       2   3           4
    #Pos    Name                    Val Identifier  Suit
    [1,     "Ace of Clubs",         11, 'A',        "♣"],
    [2,     "Ace of Spades",        11, 'A',        "♠"],
    [3,     "Ace of Diamonds",      11, 'A',        "♦"],
    [4,     "Ace of Hearts",        11, 'A',        "♥"],
    [5,     "2 of Clubs",           2,  '2',        "♣"],
    [6,     "2 of Spades",          2,  '2',        "♠"],
    [7,     "2 of Diamonds",        2,  '2',        "♦"],
    [8,     "2 of Hearts",          2,  '2',        "♥"],
    [9,     "3 of Clubs",           3,  '3',        "♣"],
    [10,    "3 of Spades",          3,  '3',        "♠"],
    [11,    "3 of Diamonds",        3,  '3',        "♦"],
    [12,    "3 of Hearts",          3,  '3',        "♥"],
    [13,    "4 of Clubs",           4,  '4',        "♣"],
    [14,    "4 of Spades",          4,  '4',        "♠"],
    [15,    "4 of Diamonds",        4,  '4',        "♦"],
    [16,    "4 of Hearts",          4,  '4',        "♥"],
    [17,    "5 of Clubs",           5,  '5',        "♣"],
    [18,    "5 of Spades",          5,  '5',        "♠"],
    [19,    "5 of Diamonds",        5,  '5',        "♦"],
    [20,    "5 of Hearts",          5,  '5',        "♥"],
    [21,    "6 of Clubs",           6,  '6',        "♣"],
    [22,    "6 of Spades",          6,  '6',        "♠"],
    [23,    "6 of Diamonds",        6,  '6',        "♦"],
    [24,    "6 of Hearts",          6,  '6',        "♥"],
    [25,    "7 of Clubs",           7,  '7',        "♣"],
    [26,    "7 of Spades",          7,  '7',        "♠"],
    [27,    "7 of Diamonds",        7,  '7',        "♦"],
    [28,    "7 of Hearts",          7,  '7',        "♥"],
    [29,    "8 of Clubs",           8,  '8',        "♣"],
    [30,    "8 of Spades",          8,  '8',        "♠"],
    [31,    "8 of Diamonds",        8,  '8',        "♦"],
    [32,    "8 of Hearts",          8,  '8',        "♥"],
    [33,    "9 of Clubs",           9,  '9',        "♣"],
    [34,    "9 of Spades",          9,  '9',        "♠"],
    [35,    "9 of Diamonds",        9,  '9',        "♦"],
    [36,    "9 of Hearts",          9,  '9',        "♥"],
    [37,    "10 of Clubs",          10, '10',       "♣"],
    [38,    "10 of Spades",         10, '10',       "♠"],
    [39,    "10 of Diamonds",       10, '10',       "♦"],
    [40,    "10 of Hearts",         10, '10',       "♥"],
    [41,    "Jack of Clubs",        10, 'J',        "♣"],
    [42,    "Jack of Spades",       10, 'J',        "♠"],
    [43,    "Jack of Diamonds",     10, 'J',        "♦"],
    [44,    "Jack of Hearts",       10, 'J',        "♥"],
    [45,    "Queen of Clubs",       10, 'Q',        "♣"],
    [46,    "Queen of Spades",      10, 'Q',        "♠"],
    [47,    "Queen of Diamonds",    10, 'Q',        "♦"],
    [48,    "Queen of Hearts",      10, 'Q',        "♥"],
    [49,    "King of Clubs",        10, 'K',        "♣"],
    [50,    "King of Spades",       10, 'K',        "♠"],
    [51,    "King of Diamonds",     10, 'K',        "♦"],
    [52,    "King of Hearts",       10, 'K',        "♥"]
    ]
stage = [1]         #Round number
max_stage = [0]     #Maximum number of rounds
score = [0]         #Total score

#Start game
print("Welcome to BlackJack\n\n")
NumberOfRounds()    #Defines number of rounds