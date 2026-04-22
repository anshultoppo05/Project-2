"""Rock-Paper-Scissors Game Module"""

import random


def get_player_choice():
    """Get valid player choice for rock-paper-scissors."""
    while True:
        choice = input("\nEnter your choice (rock/paper/scissors): ").lower().strip()
        if choice in ['rock', 'paper', 'scissors']:
            return choice
        print("Invalid choice! Please enter rock, paper, or scissors.")


def get_computer_choice():
    """Get random computer choice for rock-paper-scissors."""
    return random.choice(['rock', 'paper', 'scissors'])


def determine_winner(player, computer):
    """Determine the winner of rock-paper-scissors game."""
    if player == computer:
        return "tie"
    
    # Define winning conditions
    wins = {
        'rock': 'scissors',
        'paper': 'rock',
        'scissors': 'paper'
    }
    
    if wins[player] == computer:
        return "player"
    else:
        return "computer"


def play():
    """Main rock-paper-scissors game function."""
    print("\n" + "="*50)
    print("   ROCK - PAPER - SCISSORS GAME")
    print("="*50)
    
    player_choice = get_player_choice()
    computer_choice = get_computer_choice()
    
    print(f"\nYou chose: {player_choice}")
    print(f"Computer chose: {computer_choice}")
    
    winner = determine_winner(player_choice, computer_choice)
    
    # Display result
    if winner == "tie":
        print("\n🤝 IT'S A TIE! Well played!")
    elif winner == "player":
        print("\n🎉 YOU WIN! Great job!")
    else:
        print("\n💻 COMPUTER WINS! Better luck next time!")
    
    return winner
