true_answers = 0

while True:
    print("What is the capital of Germany?")
    first_answer = input().strip().lower()

    if first_answer == "berlin":
        print("Correct!")
        true_answers += 1
    else:
        print("The correct answer was Berlin.")


    print("How many days are there in a week?")
    second_answer = input().strip().lower()

    if second_answer == "7" or second_answer == "seven":
        print("Correct!")
        true_answers += 1
    else:
        print("The correct answer was seven.")


    print("What is 5 * 6?")
    third_answer = input().strip().lower()

    if third_answer == "30" or third_answer == "thirty":
        print("Correct!")
        true_answers += 1
    else:
        print("The correct answer was 30")


    print("Which computer language are you learning?")
    fourth_answer = input().strip().lower()

    if fourth_answer == "python":
        print("Correct!")
        true_answers += 1
    else:
        print("The correct answer was python.")


    print("What color do you get by mixing red and blue?")
    fifth_answer = input().strip().lower()

    if fifth_answer == "purple":
        print("Correct!")
        true_answers += 1
    else:
        print("The correct answer was purple.")


    print("You answered", true_answers, "out of 5 questions correctly")
    print(f"Your score is {true_answers * 20}%.")

    print("Would you like to play again?")


    while True:
        decision = input().strip().lower()
        if decision == "yes":
            print("The quiz is restarting")
            true_answers = 0
            break
        elif decision == "no":
            print("The quiz ended.")
            break
        else:
            print("Please enter yes or no.")

    if decision == "no":
        break