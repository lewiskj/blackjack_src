#Experimentation right now...
from os import system as sys            #to call 'cls'; clearing the screen
from random import choice as rand       #To clear the screen after certain calls

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

a = ['A',2,3,4,5,6,7,8,9,10,'J','Q','K']

def battleship():
    x = rand(a)
    #I could write this to a random value
    #in an array 'a certain' number of times
    #to simulate a hunting field
    print(x)



battleship()
                


