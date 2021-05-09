import random

comp = 0
player = 0

def user_selection():
    while True:
        try:
            userSelection = input("Chose 'Rock', 'Paper', 'Scissors': ").lower()
            if userSelection == 'rock' or userSelection == 'paper' or userSelection == 'scissors':
                return userSelection
            else:
                raise Exception("Please enter Rock, paper, or scissors...")
        except Exception as error:
            print(error)

def comp_ans():
    compInt = random.randint(0, 90)
    compAns = ''
    if compInt > 0 and compInt <= 30:
        compAns = "rock"
    elif compInt > 30 and compInt <= 60:
        compAns = "paper"
    else:
        compAns = "scissors"
    return compAns


def determine_winner(user_selection, comp_ans):
    global comp
    global player

    if user_selection == comp_ans:
        print("It was a draw.. Try again.")
    elif user_selection == 'rock':
        if comp_ans == 'paper':
            print("you lose.. try again")
            comp += 1
        else:
            print("you win...!")
            player += 1
    elif user_selection == 'paper':
        if comp_ans == 'scissors':
            print("You lose.. try again..")
            comp += 1
        else:
            print("you win!.!.!")
            player += 1
    elif user_selection == 'scissors':
        if comp_ans == 'paper':
            print("You win!")
            player += 1
        else:
            print("You lose..!!")
            comp += 1


def get_score():
    playerScore = player
    compScore = comp
    return f"Your score: {playerScore} --- Comp score: {compScore}"


def try_again():
    
    while True:
        tryAns = input("Would you like to try again? y/n: ").lower()
        try:
            if tryAns == 'y':
                return True
            elif tryAns == 'n':
                return False
            else:
                raise Exception("Please enter 'y' or 'n' ...")
        except Exception as error:
            print(error)

def main():
    pass #ToDO

if __name__ == '__main__':
    main()
