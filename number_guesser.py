import random

number = random.randint(1, 100)
remaining_tries = 7


while remaining_tries > 0:
    try:
        guess = int(input("Guess a number between 1-100: "))

        if guess < 1 or guess > 100:
            print("Invalid number. Give a valid number")

        elif number > guess:
            remaining_tries -= 1
            print("The actual number is bigger")
            print("Remaining tries:", remaining_tries)
        elif number < guess:
            remaining_tries -= 1
            print("The actual number is lower")
            print("Remaining tries:", remaining_tries)
        else:
            print("Your guess is right")
            break

    except ValueError:
        print("Enter a valid number")



if remaining_tries == 0:
    print("No more tries left. The number was ", number)






