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
    card1 = cardList[card]
    cardList.remove(card1)
    card2 = cardList[card]
    print("The players card is {} and the computers card is {}.\n".format(card1, card2))
    if card1 == card2:
        return
    elif card1 > card2:
        return bet
    else:
        return (bet * -1)

def roulette(guess, bet):
    print("Your bet is {} money on {}. Lets play roulette!\n".format(bet, guess))
    wheel = [00,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36]
    ball = wheel[random.randint(1, len(wheel))]
    
    if bet == "even" or bet == "black" and (bet != 0 or bet != 00):
        if (ball % 2) == 0:
            return bet
        else:
            return (bet * -1)
    elif bet == "odd" or bet == "red" and (bet != 0 or bet != 00):
        if (ball % 2) == 1:
            return bet
        else:
            return (bet * -1)
    elif bet == "1st half":
        if ball <= 18 and ball != 0 and ball != 00:
            return bet
        else:
            return (bet * -1)
    elif bet == "2nd half":
        if ball >= 19:
            return bet
        else:
            return (bet * -1)
    elif bet == "1st dozen":
        if ball <= 12 and ball != 0 and ball != 00:
            return (bet * 2)
        else:
            return (bet * -1)
    elif bet == "2nd dozen":
        if ball >= 13 and ball <= 24:
            return (bet * 2)
        else:
            return (bet * -1)
    elif bet == "3rd dozen":
        if ball >= 25:
            return (bet * 2)
        else:
            return (bet * -1)
    elif bet == "1st column":
        if (ball % 3) == 1:
            return (bet * 2)
        else:
            return (bet * -1)
    elif bet == "2nd column":
        if (ball % 3) == 2:
            return (bet * 2)
        else:
            return (bet * -1)
    elif bet == "3rd column":
        if (ball % 3) == 0 and ball != 0 and ball != 00:
            return (bet * 2)
        else:
            return (bet * -1)
    elif bet in range(36) or bet == 0 or bet == 00:
        if bet == ball:
            return (bet * 17)
        else:
            return (bet * -1)



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
            res = diceRoll(guess, bet)
        elif choice == 3:
            print("You choose High Card!\n")
            res = highCard(bet)
        elif choice == 4:
            print("You choose Roulette!\n")
            print("\nYour bet choices are: Red, Black, Even, Odd, 1st half, 2nd half   - Pays 1 to 1")
            print("\n1st dozen, 2nd dozen, 3rd dozen, 1st column, 2nd column, 3rd column   - Pays 2 to 1")
            print("\nAny single number 00 or 0 - 36   - Pays 35 to 1")
            guess = input("What would you like your bet to be?  ")
            res = roulette(guess, bet)



        if res > 0:
            money = money + res
            print("\n\nCongrats, you won! You won {} and now have {} money".format(res, money))
        elif res < 0:
            money = money + res
            print("\n\nSorry you lost. You lost {} and now have {} money".format(res, money))
        elif res == 0:
            print("\n\nIt was a tie! You have {} money".format(money))


        again = input("\nWould you like to play again (Y/N)?   ")
        again.upper()
        if again == "N":
            diff = money - 100
            print("\nThanks for playing! You have {} money which is a difference of {}".format(money, diff))
            play = False
            exit()



