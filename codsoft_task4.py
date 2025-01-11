import random

def rock_paper_scissors():
    print("Welcome to Rock-Paper-Scissors!")
    print("Instructions:")
    print("- Choose 'rock', 'paper', or 'scissors' to play.")
    print("- Type 'exit' to end the game.")

    # Initialize scores
    user_score = 0
    computer_score = 0

    # Valid choices
    choices = ["rock", "paper", "scissors"]

    while True:
        # Get user's choice
        user_choice = input("\nYour choice (rock/paper/scissors): ").lower()

        if user_choice == "exit":
            print("Thanks for playing!")
            break

        if user_choice not in choices:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue

        # Generate computer's choice
        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")

        # Determine the winner
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
            print("You win this round!")
            user_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1

        # Display scores
        print(f"Scores -> You: {user_score}, Computer: {computer_score}")

    # Final scores
    print("\nFinal Scores:")
    print(f"You: {user_score}, Computer: {computer_score}")
    if user_score > computer_score:
        print("Congratulations! You won the game!")
    elif user_score < computer_score:
        print("Computer won the game. Better luck next time!")
    else:
        print("It's a draw!")

# Run the game
rock_paper_scissors()
