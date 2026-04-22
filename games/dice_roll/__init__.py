"""Dice Roll Game - Main Module"""

from .dice import roll_dice


def play():
    """Dice roll game where player tries to beat the computer."""
    print("\n" + "="*50)
    print("   DICE ROLL GAME")
    print("="*50)
    print("\nRules: Roll dice and try to get a higher number than the computer!")
    
    # Call roll_dice function for player
    player_sum, player_rolls = roll_dice(num_dice=2, sides=6)
    print(f"\nYou rolled: {player_rolls} = {player_sum}")
    
    # Call roll_dice function for computer
    computer_sum, computer_rolls = roll_dice(num_dice=2, sides=6)
    print(f"Computer rolled: {computer_rolls} = {computer_sum}")
    
    # Determine winner
    if player_sum > computer_sum:
        print(f"\n🎉 YOU WIN! Your total ({player_sum}) > Computer's total ({computer_sum})")
        return "player"
    elif computer_sum > player_sum:
        print(f"\n💻 COMPUTER WINS! Computer's total ({computer_sum}) > Your total ({player_sum})")
        return "computer"
    else:
        print(f"\n🤝 IT'S A TIE! Both rolled {player_sum}")
        return "tie"
