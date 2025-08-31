# Rock Paper Scissors Game
# Simple Python project for beginners

import random

def get_user_choice():
    """Get and validate user's choice"""
    while True:
        print("Choose: (1) Rock, (2) Paper, (3) Scissors")
        choice = input("Enter 1, 2, or 3: ").strip()
        
        if choice == '1':
            return 'rock'
        elif choice == '2':
            return 'paper'
        elif choice == '3':
            return 'scissors'
        else:
            print("❌ Invalid choice! Please enter 1, 2, or 3.")

def get_computer_choice():
    """Generate computer's random choice"""
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    """Determine the round winner"""
    if user_choice == computer_choice:
        return 'tie'
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return 'user'
    else:
        return 'computer'

def display_result(user_choice, computer_choice, winner):
    """Display the result of the round"""
    print(f"\nYou chose: {user_choice.upper()}")
    print(f"Computer chose: {computer_choice.upper()}")
    print("---")
    
    if winner == 'tie':
        print("🤝 It's a TIE!")
    elif winner == 'user':
        print("🎉 You WIN!")
    else:
        print("💻 Computer WINS!")

def play_game():
    """Main game function"""
    # Initialize scores
    user_score = 0
    computer_score = 0
    ties = 0
    
    print("🎮 WELCOME TO ROCK PAPER SCISSORS!")
    print("==================================")
    
    while True:
        # Get choices
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        
        # Determine winner
        winner = determine_winner(user_choice, computer_choice)
        
        # Update scores
        if winner == 'user':
            user_score += 1
        elif winner == 'computer':
            computer_score += 1
        else:
            ties += 1
        
        # Display result
        display_result(user_choice, computer_choice, winner)
        
        # Show current scores
        print(f"\n📊 SCORES: You: {user_score} | Computer: {computer_score} | Ties: {ties}")
        
        # Ask to play again
        play_again = input("\nPlay again? (y/n): ").strip().lower()
        if play_again != 'y':
            break
    
    # Final results
    print("\n" + "="*30)
    print("🏁 FINAL RESULTS:")
    print(f"You won: {user_score} times")
    print(f"Computer won: {computer_score} times")
    print(f"Ties: {ties} times")
    
    if user_score > computer_score:
        print("🎊 You are the overall WINNER!")
    elif computer_score > user_score:
        print("🤖 Computer is the overall winner!")
    else:
        print("🤝 It's a overall TIE!")
    
    print("Thanks for playing! 👋")

# Run the game
if __name__ == "__main__":
    play_game()

# [Paste the complete code from the shorter version here]
