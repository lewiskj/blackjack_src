##I NEED TO:
##more CLS functions in divisible
##Exit when only one card is in the deck sooner, rather than pressing enter 1 more time
##Ace should be 1 in divisible; not 11

from os import system as sys        #RNG Function
from random import choice as rand   #To clear the screen after certain calls

def BadValue():
    sys('cls')
    print("Bad Value. Try Again.")
    #selectionScreen for launcher
    # apparently all other instances work without passing a function afterwards...?

def launcher():
    print('Card Games - Written in Python\n')

    def selectionScreen():
        while True:
            try:
                select = int(input("Select a game: "))
            
            except ValueError:
                BadValue()
                selectionScreen()
            
            except UnboundLocalError:
                BadValue()
                selectionScreen()

            if select == 1:
                blackjack_py()
            
            elif select == 2:
                divisible()

            else:
                BadValue()
                selectionScreen()

    selectionScreen()

def blackjack_py():
    #Defining Programs
    def play_blackjack():
        #Cache flushed each round, but not each card draw
        rngroll = []                #saves ~76 characters over defining outright                
        for number in range(0,52):  #takes 1-52...
            rngroll.append(number)  #and creates the table out of it
            
        aceCount = [0]             #number of ace cards
        hand = [0]             #your hand; [0] is value and [1:] are the cards
        
        cache = [
            ["|¯¯¯¯¯¯˥"],   #0
            [],             #1 Identifier
            [],             #2 Suit
            [],             #3 Suit
            [],             #4 Identifier
            ["|______˩"],   #5
        ]                   #Could be global? But prefer to keep each game seperate
        
        def scorecheck():
            if stage[0] > max_stage[0]:
                sys('cls')
                print("You've completed your last round. Final score: " + str(score[0]))
                while True:
                    try:
                        playAgain = int(input("Do you want to play again? [no] or 1 for yes:\n"))
                    
                    except ValueError:
                        launcher()

                    if playAgain == 1:
                        NumberOfRounds()
                    
                    else:
                        launcher()
                
            else:
                sys('cls')
                print("\nRound " + str(stage)[1:-1] + " of " + str(max_stage)[1:-1])
                print("Total Score: " + str(score[0]))
                print("\nYour Hand (" + str(hand[0]) + "/21): " + ", ".join(hand[1:]))
                if hand[0] > 1:
                    print("Last Card Drawn:")
                    for y in cache:
                        print("".join(y))
        
            #if game continues, check value of hand
            if int(hand[0]) == 21: 
                print("You Win!")
                input("Press Enter to go to the next round... ")
                eor_scoring()
            
            elif hand[0] > 21:
                #Ace check; if you don't have one the game is over
                if aceCount[0] == 0:
                    print("You got over 21!")
                    input("Press Enter to go to the next round...")
                    eor_scoring()

                #Ace check; if you have an ace your hand value drops by 10 and the game resumes
                elif aceCount[0] > 0:
                    print("You got over 21, but you drew one or more Aces. One of them has been devalued to let you keep drawing")
                    
                    #devalues a single ace by 10, removes it from the deck, then continues
                    hand[0] -= 10
                    aceCount[0] -= 1
                    scorecheck()
        
            #if hand not equal to or greater than 21, ask to draw a card
            else:
                card = [0]
                while True:
                    try:
                        card[0] = int(input("Draw Card? 1 for yes, or 2 to end the round:\n"))
                    except ValueError:
                        BadValue()
                    if card[0] == int(1):
                        drawcard()
                    elif card[0] == int(2):
                        eor_scoring()
                    else:
                        BadValue()
        
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


    #Static Variables; are not flushed after each round

    def NumberOfRounds():
        sys('cls')
        print("Welcome to BlackJack\n\n")
        while True:
            try:
                max_stage[0] = int(input("Select number of rounds:\n"))
            except ValueError:
                BadValue()
            if max_stage[0] < 1:
                BadValue()
            else:
                play_blackjack()

    
    stage = [1]         #Round number
    max_stage = [0]     #Maximum number of rounds
    score = [0]         #Total score

    #Start game
    NumberOfRounds()

def divisible():
    #Importing Needed Modules

    def play_divisible():   
        
        ##flushed each round##
        hand = [0]          #your hand; index 0 not used but easier to leave be; 1: are the textual names
        value = [0]
        ## ##

        remainderZero = [0]   #not flushed

        rngroll = []                #when this is emptied, game over                               
        for number in range(0,52):  #takes 1-52...
            rngroll.append(number)  #and creates the table out of it
            
        cache = [
            ["|¯¯¯¯¯¯˥"],   #0
            [],             #1 Identifier
            [],             #2 Suit
            [],             #3 Suit
            [],             #4 Identifier
            ["|______˩"],   #5
            #Used to 'visually' (Unicode chars.) draw a card on screen
        ]
            
        def scorecheck():
            while True:     #a few lines to prompt user before drawing a card
                try:
                    input("\nPress any key to draw three cards:\n" + "~"*25) #~*25 for clarity inbetween draws
                except ValueError:
                    drawcard()
                else:
                    drawcard()

        def drawcard():
            #sys('cls')

            for itterate in range(1,4): #draws 3 cards
                try:
                    x = rand(rngroll)   #prevents double rolling    
                    rngroll.remove(x)   #prevents double rolling
                    
                    hand.append(deck[x-1][1])   #Appends the textual name of the card
                    value[0] += deck[x-1][2]    #Appends the numerical value of the card
                    visual_cards()              #Draws card on screen
                
                except IndexError:              #Can't draw 3 cards? Game over.
                    print("You're all out of cards! The card you didn't draw was the " + str(hand[1]))
                    print("Final net score: " + str(remainderZero[0]) + "\n")
                    launcher()

            additives = 0
            for x in deck:
                if str(hand[1]) in x:
                    additives += x[2]
                
                elif str(hand[2]) in x:
                    additives += x[2]

                elif str(hand[3]) in x:
                    divisor = x[2]            

            print("\nLast Cards Drawn: " + ", ".join(hand[1:]))

            print("Additives: " + str(additives))
            print("Divisor: " + str(divisor))
            
            if int(additives)%int(divisor) == 0:    #Is the remainder 0?
                remainderZero[0] += 1               #Yes; +=1
                print("Your cards divide evenly! Score +1; " + str(remainderZero[0]))
            
            else:
                remainderZero[0] -= 1               #No; -=1
                print("Your cards did not divide evenly. Score -1; " + str(remainderZero[0]))

            del hand[1:]         
            divisor = 0

            scorecheck()

        def visual_cards():
            for y in deck:                          #10 is two characters instead of the usual 1; catch that
                if y[1] in hand[-1:]:
                    if '10 of ' in y[1]:
                        cache[1] = "|10    |"
                        cache[4] = "|    10|"   

                    else:
                        cache[1] = str("|" + y[3] + "     |")   #Normal top and bottom lines
                        cache[4] = str("|     " + y[3] + "|")
                
                    cache[2] = str("|" + y[4] + "     |")       #Normal middle lines
                    cache[3] = str("|     " + y[4] + "|")    

            for z in cache:
                print("".join(z))

        #start game
        scorecheck()

    play_divisible()

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
#############################

launcher()