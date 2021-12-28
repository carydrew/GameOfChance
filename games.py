import random

money = 100                     
      

#Write your game of chance functions here

def coinFlip(guess, bet): 
    try:
        guess = int(guess)
        while guess > 1 or guess < 0:
            print("Please make a valid guess.\n\nHeads = 0\nTails = 1")
            guess = input("Your choice: ")
            try:
                guess = int(guess)
            except:
                print("Please ensure your guess is 0 or 1.\n")
        print("Your bet is {}. Lets flip the coin!\n".format(bet))
        guess = int(guess)
        num = random.randint(1,10)
        result = num % 2
        if guess == result:
            return bet
        else:
            return (bet * -1)
    except:
        print("Please make a valid guess.\n\nHeads = 0\nTails = 1")
        guess = input("Your choice: ")
        coinFlip(guess, bet)
    
def diceRoll(guess, bet):
    try:
        guess = int(guess)
        while guess > 1 or guess < 0: 
            print("Please make a valid guess.\nEven = 0\nOdd = 1")
            guess = input("Your choice: ")
            try:
                guess = int(guess)
            except: 
                print("Please ensure your guess is 0 or 1.\n")
        print("Your bet is {}. Lets roll the dice!\n".format(bet))
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        print("The dice are {} and {}.\n".format(dice1, dice2))
        result = (dice1 + dice2) % 2
        if guess == result:
            return bet
        else:
            return (bet * -1)
    except:
        print("Please make a valid guess.\nEven = 0\nOdd = 1")
        guess = input("Your choice: ")
        diceRoll(guess, bet)

def highCard(bet):
    cardList = [2,3,4,5,6,7,8,9,10,11,12,13,14,2,3,4,5,6,7,8,9,10,11,12,13,14,2,3,4,5,6,7,8,9,10,11,12,13,14,2,3,4,5,6,7,8,9,10,11,12,13,14]
    print("Lets play High card! In this game the Ace card is High!")
    print("The face cards are label as follows:\nJ: 11\nQ: 12\nK: 13\nA: 14\n")
    card1 = cardList[random.randint(1, len(cardList))]
    cardList.remove(card1)
    card2 = cardList[random.randint(1, len(cardList))]
    print("The players card is {} and the computers card is {}.".format(card1, card2))
    if card1 == card2:
        return
    elif card1 > card2:
        return bet
    else:
        return (bet * -1)

def roulette(guess, bet):
    while True:
        
        wheel = [00,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36]
        red = [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]
        ball = wheel[random.randint(0, len(wheel) -1)]
        guessList = ["red","black","even","odd","1st half","2nd half","1st dozen","2nd dozen","3rd dozen","1st column","2nd column","3rd column"]

        # Figure out the ball
        def ball_func(): 
            if ball == 0 or ball == 00:
                print("\nThe ball landed on: {}\n".format(ball))
                return
            else:
                if (ball % 2) == 0:
                    EorO = "even"
                elif(ball % 2) == 1:
                    EorO = "odd"
                if ball in red:
                    color = "red"
                else:
                    color = "black"
                print("\nThe ball landed on: {} Which is {} and {}.\n".format(ball, color, EorO))
                return color, EorO

        # Fix the guess
        try:
            guess = int(guess)
            if guess not in wheel:
                print("Please make a valid guess!")
                guess = input("What is your guess: ")
                continue
            elif guess in wheel:
                print("Your bet is {} on {}. Lets play roulette!".format(bet, guess))
                ball_func()
                if ball == guess:
                    return (bet * 17)
                else:
                    return (bet * -1)

            else:
                print("What")
        finally:
            guess = guess.lower()

            # Confirm string guess 
            if guess not in guessList:
                print("Please make a valid guess.")
                guess = input("What is your guess: ")
                continue
            elif guess in guessList:
                print("Your bet is {} on {}. Lets play roulette!!".format(bet, guess))
                color, EorO = ball_func()

            # Win/Lose functions
            if guess == "red" or guess == "black":
                if guess == color:
                    return bet
                else:
                    return (bet * -1)
            elif guess == "even" or guess == "odd":
                if guess == EorO:
                    return bet
                else:
                    return (bet * -1)
            elif guess == "1st half":
                if ball <= 18 and ball > 0:
                    return bet
                else:
                    return (bet * -1)
            elif guess == "2nd half":
                if ball >= 19:
                    return bet
                else:
                    return (bet * -1)
            elif guess == "1st dozen":
                if ball <= 12 and ball > 0:
                    return (bet * 2)
                else:
                    return (bet * -1)
            elif guess == "2nd dozen":
                if ball >= 13 and ball <= 24:
                    return (bet * 2)
                else:
                    return (bet * -1)
            elif guess == "3rd dozen":
                if ball >= 25:
                    return (bet * 2)
                else:
                    return (bet * -1)
            elif guess == "1st column":
                if (ball % 3) == 1:
                    return (bet * 2)
                else:
                    return (bet * -1)
            elif guess == "2nd column":
                if (ball % 3) == 2:
                    return (bet * 2)
                else:
                    return (bet * -1)
            elif guess == "3rd column":
                if (ball % 3) == 0 and ball > 0:
                    return (bet * 2)
                else:
                    return (bet * -1)
            else: 
                print("Please make a valid guess to bet on.")
                guess = input("What is your guess? ")
                continue
            


def exitGame():
    diff = money - 100
    print("\nThanks for playing! You have {} money which is a difference of {}".format(money, diff))
    exit()

def get_bet():
    while True:
        bet = input("You currently have {} money.\nYour bet is: ".format(money))
        try:
            bet = int(bet)
            if bet > money:
                print("You don't have that much money. Please make a bet with the money you do have.")
                continue
            return bet
        except:
            print("Please make a valid bet")
        

#Call your game of chance functions here

if __name__ == "__main__":
    print("Welcome to the games of chances! \n")
    while money > 0:

        print("Which Game would you like to play?\n")
        print("1: Coin Flip\n2: Dice roll\n3: High Card\n4: Roulette\n0: Quit Playing\n")
        choice = input("Enter the numerical value of your choice: ")
        try:
            choice = int(choice)
        except:
            print("Please make a valid numerical choice\n")
            continue
        if choice == 0:
            exitGame()

        bet = get_bet()

        if choice == 1:
            print("You choose Coin Flip!\n")
            guess = input("Do you think it will be heads or tails?\nHeads = 0\nTails = 1\nYour choice: ")
            res = coinFlip(guess, bet)
        elif choice == 2:
            print("You choose Dice Roll!\n")
            guess = input("Do you think it will be even or odd?\nEven = 0\nOdd  = 1\nYour choice: ")
            res = diceRoll(guess, bet)
        elif choice == 3:
            print("You choose High Card!\n")
            res = highCard(bet)
        elif choice == 4:
            print("You choose Roulette!\n")
            print("Your bet choices are: \nRed, Black, Even, Odd, 1st half, 2nd half   - Pays 1 to 1")
            print("1st dozen, 2nd dozen, 3rd dozen, 1st column, 2nd column, 3rd column   - Pays 2 to 1")
            print("Any single number 00 or 0 - 36   - Pays 35 to 1")
            guess = input("\nWhat would you like your guess to be?  ")
            res = roulette(guess, bet)
        else:
            print("Please make a valid choice.")
            continue


        res = int(res)
        if res > 0:
            money = money + res
            print("\n\nCongrats, you won! You won {} and now have {} money".format(res, money))
        elif res < 0:
            money = money + res
            print("\n\nSorry you lost. You lost {} and now have {} money".format(res, money))
        elif res == 0:
            print("\n\nIt was a tie! You have {} money".format(money))

        if money <=0:
            print("Sorry, your ran out of money. Please come back when you can afford it.")
            exit()

        again = input("\nWould you like to play again (Y/N)?   ")
        if again.upper() == "N" or again.upper() == "NO":
            exitGame()
    
    
            



