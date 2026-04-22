"""Determine winner for Rock-Paper-Scissors"""


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
