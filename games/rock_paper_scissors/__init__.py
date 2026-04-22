"""Rock-Paper-Scissors Game - Main Module"""

from .player_choice import get_player_choice
from .computer_choice import get_computer_choice
from .winner import determine_winner


def play():
    """Main rock-paper-scissors game function."""
    print("\n" + "="*50)
    print("   ROCK - PAPER - SCISSORS GAME")
    print("="*50)
    
    # Call player_choice function
    player_choice = get_player_choice()
    
    # Call computer_choice function
    computer_choice = get_computer_choice()
    
    print(f"\nYou chose: {player_choice}")
    print(f"Computer chose: {computer_choice}")
    
    # Call winner determination function
    winner = determine_winner(player_choice, computer_choice)
    
    # Display result
    if winner == "tie":
        print("\n🤝 IT'S A TIE! Well played!")
    elif winner == "player":
        print("\n🎉 YOU WIN! Great job!")
    else:
        print("\n💻 COMPUTER WINS! Better luck next time!")
    
    return winner
