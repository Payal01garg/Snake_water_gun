import random


def game():
    user_score = 0
    while True:
        user = input("Enter 'snake', 'water', or 'gun': ")
        computer = random.choice(['snake', 'water', 'gun'])

        print(f"Computer's choice: {computer}")

        if user == computer:
            print("It's a tie! Try again.")
        elif user == 'snake':
            if computer == 'water':
                print("You win!")
                user_score += 1
            else:
                print("You lose! Try again.")
                break
        elif user == 'water':
            if computer == 'gun':
                print("You win!")
                user_score += 1
            else:
                print("You lose! Try again.")
                break
        elif user == 'gun':
            if computer == 'snake':
                print("You win!")
                user_score += 1
            else:
                print("You lose! Your final score is: ", user_score)
                break
        else:
            print("Please enter a valid option: 'snake', 'water', or 'gun'")


# Start the game
game()
