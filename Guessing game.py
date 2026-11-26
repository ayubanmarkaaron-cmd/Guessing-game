import random

number = random.randint(1, 100)

print("Welcome to the Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
print("You have chances to get the correct number.\n")

difficulty = ""
chances = 0
attempts = 0

    
while True:
    print("Please select the difficulty level:")
    print("1. Easy (10 chances)")
    print("2. Medium (5 chances)")
    print("3. Hard (3 chances)")
    
    
    choice = input('Enter your choice or Enter "quit" to exit: ')

    if choice == "1":
        chances = 10
        difficulty = "Easy"
    elif choice == "2":
        chances = 5
        difficulty = "Medium"
    elif choice == "3":
        chances = 3
        difficulty = "Hard"
    elif choice == "quit":
        print("Thank you for playing.")
        break
    else:
        print("Invalid input.")
        continue
        
    print("\nGreat! You have selected the _ difficulty level.")
    print("Let's start the game!\n")
    
    while True:
        if chances == 0:
            print("Oops, You have no chances left.")
            break
        
        print("Chances:", chances)
        guess = int(input("Enter your guess: "))

        if guess > 0 and guess <= 100:
            if guess > number:
                print(f"Incorrect! The number is less than {guess}.\n")
                chances -= 1
                attempts += 1
            elif guess < number:
                print(f"Incorrect! The number is greater than {guess}.\n")
                chances -= 1
                attempts += 1
            else:
                print(f"Congratulations! You guess the correct number in {attempts} attempts.")
                break
        else:
            print("Guess 1 to 100 only.")
    print(f"The number is {number}.\n")

    # I put it for new number :)
    number = random.randint(1, 100)