import random

choices = ['r','p','s']

while True:
        computer_choice = random.choice(choices)
        user_choice = input("Rock Paper Scissor(r/p/s)?? :").lower()
        if user_choice not in choices:
            print("Invalid input!!!\n")
            continue

        print(f"\nComputer's choice ={computer_choice}")
        print(f"User's choice     ={user_choice}")

        if computer_choice == user_choice:
            print("Both choose the same so it is a Draw!\n")

        elif computer_choice == 'r' and user_choice == 'p':
            print("User wins....\n")
        elif computer_choice == 'p' and user_choice == 's':
            print("User wins....\n")
        elif computer_choice == 's' and user_choice == 'r':
            print("User wins....\n")

        else:
            print("Computer wins...\n")

        continuing = input("Do you want to continue??(y/n): ").lower()
        if continuing == 'n':
            print("Thanks for playing the game.")

