import random

computerChoice = random.choice(['rock', 'paper', 'scissors'])
playerChoice = input("Please select one of rock, paper or scissors:").strip().lower()

if playerChoice not in ['rock', 'paper', 'scissors']:
    print("Your input is invalid")
else:
    print("Computer's choice is ",computerChoice, "your choice is ",playerChoice)

    if computerChoice == 'rock' and playerChoice == 'paper':
        print("Congratulations you won")
    elif computerChoice == 'rock' and playerChoice == 'scissors':
        print("Sorry you lost")
    elif computerChoice == 'scissors' and playerChoice == 'rock':
        print("Congratulations you won")
    elif computerChoice == 'scissors' and playerChoice == 'paper':
        print("Sorry you lost")
    elif computerChoice == 'paper' and playerChoice == 'scissors':
        print("Congratulations you won")
    elif computerChoice == 'paper' and playerChoice == 'rock':
        print("Sorry you lost")
    else:
        print("It's a draw")