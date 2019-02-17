from IPython.display import clear_output
from random import randint
import time

class Blackjack():
    def __init__(self, rows, cols, game_over, flagInit):
        self.rows = rows
        self.cols = cols
        self.game_over = game_over
        self.flagInit = flagInit

    def showGrid(self):
        print('Dealer:\t\tPlayer:                ')
        print('-----------------------------------')
        for i in range(max(len(dealer.hand),len(player.hand))):
            if i == 1 and self.flagInit == True:
                print('-----------\t{}'.format(player.hand[i]))
            elif i>(len(dealer.hand)-1):
                print('\t\t{}'.format(player.hand[i]))
            elif i>(len(player.hand)-1):
                print('{}'.format(dealer.hand[i]))
            else:
                print('{}\t{}'.format(dealer.hand[i], player.hand[i]))
        print('-----------------------------------')

        if self.flagInit == True:
            if dealer.hand[0][0:1] == 'J' or dealer.hand[0][0:1] == 'Q' or dealer.hand[0][0:1] == 'K':
                print('Total: 10\tTotal: {}'.format(player.total))
            elif dealer.hand[0][0:1] == 'A':
                print('Total: 11\tTotal: {}'.format(player.total))
            else:
                print('Total: {}\tTotal: {}'.format(dealer.hand[0][0:2], player.total))
        elif self.flagInit==False:
            print('Total: {}\tTotal: {}'.format(dealer.total, player.total))

    def drawCard(self):
        # randomly generate a playing card value
        t_num=('A',2,3,4,5,6,7,8,9,10,'J','Q','K')
        t_suit=('Hearts', 'Spades', 'Diamonds', 'Clubs')
        rand_num = randint(0,12)
        rand_suit = randint(0,3)
        num = t_num[rand_num]
        suit = t_suit[rand_suit]
        time.sleep(0.01)
        self.num = str(num)
        self.suit = suit
        if num == 'A':
            self.num_val = int(11)
        elif num == 'J' or num == 'Q' or num == 'K':
            self.num_val = int(10)
        else:
            self.num_val = int(num)
        return self.num, self.num_val, self.suit

    def flag(self):
        self.flagInit = False

    def startGame(self):
        print('Welcome to Blackjack!\n\nAt the beginning of the round, the player and the dealer each receive two cards: '+
              'the player\'s cards are both dealt face up, while the dealer has one face up and the second face down. '+
              'The object of the game is to score as close to 21 points as possible without going over.\n\nNumeral cards '+
              '2 to 10 have their face values. Jacks, Queens and Kings are valued at 10, and Aces are valued at 11 unless '+
              'that would result in the hand going over 21, in which case the ace becomes valued at 1.\n\nA starting hand '+
              'of a 10-valued card and an Ace is called a \"Blackjack\" and beats all hands, other than another Blackjack.'+
              ' If the player and dealer both have Blackjack, the result is a \"push\" (i.e. tie).\n\nIf the player '+
              'is happy with the total they’ve been dealt they can \"stay\", taking no further action and passing to the '+
              'dealer. If the player wishes to take another card, they can \"hit\", and a single card is then played face '+
              'up onto their hand. While the hand total is less than 21, the player can choose to \"hit\" again or '+
              '\"stay\". If the total is over 21, the hand is a \"bust\" and the player loses.\n\nOnce the player has '+
              'decided to \"stay\", the dealer reveals their face-down card and continues to take cards until they have '+
              'a total of 17 or higher. If the dealer \"busts\" (i.e. total goes over 21), the player automatically wins. '+
              'Otherwise, whoever has a higher total wins. A tie is a \"push\" and neither the player nor dealer wins or '+
              'loses.')
        time.sleep(0.01)
        while True:
            ans = input('Enter any key, then \'enter\' to start playing: ')
            player.total = 0
            player.count = 0
            dealer.total = 0
            dealer.count = 0
            player.hand = []
            dealer.hand = []
            clear_output()
            if ans:
                player.dealNext() # deals 1st card to player
                dealer.dealNext() # deals 1st card to dealer (face up)
                player.dealNext() # deals 2nd card to player
                dealer.dealNext() # deals 2nd card to dealer (face down)
                break

        self.showGrid()
        time.sleep(0.01)
        self.checkStatus()


    def askMove(self):
        time.sleep(0.01)
        ans = input('Would you like to hit or stay? ')
        if ans.lower()[0] == 'h':
            clear_output()
            player.dealNext()
            self.showGrid()
            self.checkStatus()
        elif ans.lower()[0] == 's':
            clear_output()
            self.flag()
            self.showGrid()
            self.checkDealer17()
            self.checkStatus()
        elif ans.lower()[0] == 'q':
            self.game_over = True
        else:
            print('Not a valid option')

    def checkDealer17(self):
        while dealer.total < 17:
            clear_output()
            dealer.dealNext()
            game.showGrid()
            game_over = False

    def checkStatus(self):
        if player.total == 21:
            clear_output()
            self.flag()
            self.showGrid()
            self.checkDealer17()
            if dealer.total == 21:
                print('\nPUSH! The dealer and player have tied.')
                self.game_over = True
            else:
                print('\nYou WIN!! Your total is 21.')
                self.game_over = True
        elif player.total > 21:
            print('\nBUST! Your total is greater than 21.')
            self.game_over = True
        elif self.flagInit == True:
            self.askMove()
        elif self.flagInit == False:
            if dealer.total == 21:
                print('\nYou LOSE!! Dealer\'s total is 21.')
                self.game_over = True
            elif dealer.total > 21 and player.total<21:
                print('\nYou WIN!! Dealer busts.')
                self.game_over = True
            elif player.total > dealer.total and player.total < 21:
                print('\nYou WIN!! Your total is closer to 21 than the dealer\'s.')
                self.game_over = True
            elif dealer.total > player.total and dealer.total > 17:
                print('\nYou LOSE!! Dealer\'s total is closer to 21 than player\'s.')
                self.game_over = True
            elif player.total == dealer.total:
                print('\nPUSH! The dealer and player have tied.')
                self.game_over = True

class Player():
    def __init__(self):
        self.total = 0
        self.count = 0
        self.count_ace = 0
        self.hand = []

    def dealNext(self):
        game.drawCard()
        card = str(game.num) + ' of ' + (game.suit)
        self.hand.append(card)
        self.count += 1
        self.total = self.total + game.num_val

        for i in range(len(self.hand)):
            if i>0 and self.hand[i][0]=='A' and self.total>21:
                self.count_ace += 1
        if self.total > 21:
            self.total -= (10*self.count_ace)

class Dealer():
    def __init__(self):
        self.total = 0
        self.count = 0
        self.count_ace = 0
        self.hand = []

    def dealNext(self):
        game.drawCard()
        card = str(game.num) + ' of ' + (game.suit)
        self.hand.append(card)
        self.count += 1
        self.total = self.total + game.num_val

        for i in range(len(self.hand)):
            if i>0 and self.hand[i][0]=='A' and self.total>21:
                self.count_ace += 1
        if self.total > 21:
            self.total -= (10*self.count_ace)


# START OF MAIN LOOP
while True:
    # define global variables to be used
    game = Blackjack(2,2,game_over = False,flagInit = True)
    player = Player()
    dealer = Dealer()
    game.startGame()

    while game.game_over != True:
        time.sleep(0.01)
        game.askMove()

    time.sleep(0.01)
    ans = input('\nWould you like to play again(yes/no)? ')

    # base case
    if ans.lower()[0] == 'n' or ans.lower()[0] == 'q':
        print('Thanks for playing!')
        break
    elif ans.lower()[0] == 'y':
        clear_output()
        game.game_over = False
    else:
        print('***options are yes or no***')
