import random

mysterious_number = random.randint(1, 10)

prediction = int(input("Please enter a number:"))

if prediction == mysterious_number:
    print("Your prediction is correct")

else:
    print("Your prediction is not correct")
    print("The real number is ", mysterious_number)