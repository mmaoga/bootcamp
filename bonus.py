# #-----------------------------------------------------------------------
# # deal.py
# #-----------------------------------------------------------------------

# import stdio
# import sys
# import random

# # Accept integer playerCount as a command-line argument. Deal 5-card
# # hands at random to playerCount players. Write the hands to standard
# # output.

# CARDS_PER_PLAYER = 5

# playerCount = int(sys.argv[1])

# # Initialize the deck.
# suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
# ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', \
#     'Jack', 'Queen', 'King', 'Ace']
# deck = []
# for rank in ranks:
#     for suit in suits:
#         card = rank + ' of ' + suit
#         deck += [card]

# # Shuffle the deck.
# for i in range(len(deck)):
#     r = random.randrange(i, len(deck))
#     temp = deck[r]
#     deck[r] = deck[i]
#     deck[i] = temp

# # Write cards from the shuffled deck.
# deckIndex = 0
# for i in range(playerCount):
#     for j in range(CARDS_PER_PLAYER):
#         stdio.writeln(deck[deckIndex])
#         deckIndex += 1
#     stdio.writeln()
    
# #-----------------------------------------------------------------------

# # python deal.py 1              
# # 10 of Hearts
# # 7 of Clubs
# # 9 of Diamonds
# # Queen of Hearts
# # 3 of Spades

# # python deal.py 4
# # Jack of Hearts
# # Queen of Hearts
# # 7 of Spades
# # 3 of Hearts
# # 5 of Clubs
# # 
# # King of Diamonds
# # Queen of Spades
# # 8 of Hearts
# # 9 of Diamonds
# # 6 of Spades
# # 
# # 3 of Diamonds
# # 9 of Clubs
# # Jack of Spades
# # 9 of Spades
# # 5 of Hearts
# # 
# # Queen of Diamonds
# # 10 of Clubs
# # 2 of Clubs
# # King of Hearts
# # 5 of Diamonds


# #first let's import random procedures since we will be shuffling
# import random

# #next, let's start building list holders so we can place our cards in there:
# cardfaces = []
# suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
# royals = ["J", "Q", "K", "A"]
# deck = []

# #now, let's start using loops to add our content:
# for i in range(2,11):
#     cardfaces.append(str(i))
#     #this adds numbers 2-10 and converts them to string data

# for j in range(4):
#     cardfaces.append(royals[j])
#     #this will add the royal faces to the cardbase

# #cool, it works so far. Now we need to "attach" the suits to it
# #this gets a little tricky

# for k in range(4):
#     for l in range(13):
#         card = (cardfaces[l] + " of " + suits[k])
#         #this makes each card, cycling through suits, but first through faces
#         deck.append(card)
#         #this adds the information to the "full deck" we want to make
# #now let's shuffle our deck!
# random.shuffle(deck)

# #now let's see the cards!
# for m in range(52):
#     print(deck[m])


# #I also want to see what the deck looks like before shuffling. We should have
#     #done that a while ago... oh well!




    #first let's import random procedures since we will be shuffling
import random

#next, let's start building list holders so we can place our cards in there:
# cardfaces = []
suits = ["Hearts", "Spades", "Clubs", "Diamonds"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
deck = []

for suit in suits:
    for rank in ranks:
        deck.append(f'{rank} of {suit}')


print (f'There are {len(deck)} cards in the deck.')
print ()
print ("Dealing........")
print()

player_1 = []
player_2 = []

while len(player_1)<5:
    card = random.choice (deck)
    deck.remove (card)
    player_1.append(card)
    card_2 = random.choice(deck)
    deck.remove(card_2)
    player_2.append(card_2)

print (f'There are now {len(deck)} cards in the deck.')
print ()
print ("Player1 has the following cards in their hand: ")
print (player_1)
print ()
print ("Player2 has the following cards in their hand: ")
print (player_2)
print ()







