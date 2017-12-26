#Rock, Paper, Scissors game.
import random
import string


print('\033[1m',  "\nWelcome to the Rock, Paper, Scissors game. \nPlay against the computer to become the champion!\n")
options = ['Rock', 'Paper', 'Scissors']



while True:
    print("Rock, \nPaper,")
    userChoice = str(input('...: ')).capitalize()
    #val = random.randint(0, 2)
    computerChoice = random.choice(options)#options[val]

#Error handling

    if userChoice.capitalize() in options:
            if userChoice == 'Rock' and computerChoice == 'scissors':
                print("The computer chose", computerChoice)
                print("You win, Well done!")
                break
            elif userChoice == 'Paper' and computerChoice == 'Scissors':
                print("The computer chose", computerChoice)
                print("You lose, better luck nex time!")
                break
            elif userChoice == 'Rock' and computerChoice == 'Paper':
                print("The computer chose", computerChoice)
                print("You lose, better luck nex time!")
                break
            elif userChoice == 'Paper' and computerChoice == 'Rock':
                print("The computer chose", computerChoice)
                print("You win, Congratulations!")
                break
            #elif userChoice == 'Scissors' and computerChoice == 'Scissors':
                print("The computer chose", computerChoice)
                print("It's a scissor sword fight! You batlle hard and it ends up a draw!")
                break
            elif userChoice == 'Scissors' and computerChoice == 'Rock':
                print("The computer chose", computerChoice)
                print("You lost, better luck next time!")
                break
            elif userChoice == 'Scissors' and computerChoice == 'Paper':
                print("The computer chose", computerChoice)
                print("You win, Congratulations!")
                break
            elif userChoice == computerChoice:
                print("The computer also chose", computerChoice)
                print("It's a draw, try again!\n")
                userChoice = ""
                continue
    else:
        print("\nPlease enter either:", options[0], options[1], options[2] + "\n")
