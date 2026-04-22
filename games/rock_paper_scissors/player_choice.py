"""Get player choice for Rock-Paper-Scissors"""


def get_player_choice():
    """Get valid player choice for rock-paper-scissors."""
    while True:
        choice = input("\nEnter your choice (rock/paper/scissors): ").lower().strip()
        if choice in ['rock', 'paper', 'scissors']:
            return choice
        print("Invalid choice! Please enter rock, paper, or scissors.")
