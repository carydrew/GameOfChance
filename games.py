import random

money = 100                     # int
num = random.randint(1,10)      # int 
dice = random.randint(1,6)

#Write your game of chance functions here

def coinFlip(guess, bet): # guess is a 1 or 2, bet is the amount.
    print("Your bet is {}. Lets flip the coin!\n".format(bet))
    result = num % 2
    if guess == result:
        return bet
    else:
        return (bet * -1)

def diceRoll(guess, bet):
    print("Your bet is {}. Lets roll the dice!\n".format(bet))
    dice1 = dice
    dice2 = dice
    print("The dice are {} and {}\n".format(dice1, dice2))
    result = (dice1 + dice2) % 2

    if guess == 2:        # Change even bet to 0 for modulo
        guess = 0
    
    if guess == result:
        return bet
    else:
        return (bet * -1)

def highCard(bet):
    cardList = [2,3,4,5,6,7,8,9,10,11,12,13,14,2,3,4,5,6,7,8,9,10,11,12,13,14,2,3,4,5,6,7,8,9,10,11,12,13,14,2,3,4,5,6,7,8,9,10,11,12,13,14]
    card = random.randint(1, len(cardList))
    print("Lets play High card! In this game the Ace card is High!\n")
    card1 = card
    cardList.remove(card1)
    card2 = card
    print("The players card is {} and the computers card is {}.\n".format(card1, card2))
    if card1 == card2:
        return
    elif card1 > card2:
        return bet
    else:
        return (bet * -1)

def roulette(guess, bet):
    print("Your bet is {}. Lets play roulette!\n".format(bet))



#Call your game of chance functions here

if __name__ == "__main__":
    print("Welcome to the games of chances! \n")
    play = True
    while money > 0 and play == True:

        print("Which Game would you like to play?\n")
        print("1: Coin Flip\n2: Dice roll\n3: High Card\n 4: Roulette\n")
        choice = input("Enter the numerical value of your choice: ")
        bet = input("You currently have {} money.\nYour bet is: ".format(money))

        if choice == 1:
            print("You choose Coin Flip!\n")
            guess = input("Do you think it will be heads or tails?\nHeads = 0\nTails = 1\nYour choice: ")
            res = coinFlip(guess, bet)
        elif choice == 2:
            print("You choose Dice Roll!\n")
            guess = input("Do you think it will be even or odd?  ")
            res = coinFlip(guess, bet)



        if res > 0:
            money = money + res
            print("Congrats, you won! You won {} and now have {} money".format(res, money))
        elif res < 0:
            money = money + res
            print("Sorry you lost. You lost {} and now have {} money".format(res, money))
        elif res == 0:
            print("It was a tie! You have {} money".format(money))


        again = input("Would you like to play again (Y/N)?   ")
        again.upper()
        if again == "N":
            diff = money - 100
            print("Thanks for playing! You have {} money which is a difference of {}".format(money, diff))
            play = False
            exit()



