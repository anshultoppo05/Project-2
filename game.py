import random

# ==================== ROCK-PAPER-SCISSORS GAME ====================

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


def determine_winner_rps(player, computer):
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


def play_rock_paper_scissors():
    """Main rock-paper-scissors game function."""
    print("\n" + "="*50)
    print("   ROCK - PAPER - SCISSORS GAME")
    print("="*50)
    
    player_choice = get_player_choice()
    computer_choice = get_computer_choice()
    
    print(f"\nYou chose: {player_choice}")
    print(f"Computer chose: {computer_choice}")
    
    winner = determine_winner_rps(player_choice, computer_choice)
    
    # Display result
    if winner == "tie":
        print("\n🤝 IT'S A TIE! Well played!")
    elif winner == "player":
        print("\n🎉 YOU WIN! Great job!")
    else:
        print("\n💻 COMPUTER WINS! Better luck next time!")
    
    return winner


# ==================== DICE ROLL GAME ====================

def roll_dice(num_dice=1, sides=6):
    """Roll dice and return the sum."""
    rolls = [random.randint(1, sides) for _ in range(num_dice)]
    return sum(rolls), rolls


def play_dice_roll():
    """Dice roll game where player tries to beat the computer."""
    print("\n" + "="*50)
    print("   DICE ROLL GAME")
    print("="*50)
    print("\nRules: Roll a dice and try to get a higher number than the computer!")
    
    # Player rolls
    player_sum, player_rolls = roll_dice(num_dice=2, sides=6)
    print(f"\nYou rolled: {player_rolls} = {player_sum}")
    
    # Computer rolls
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


# ==================== MAIN MENU ====================

def display_menu():
    """Display the main menu."""
    print("\n" + "="*50)
    print("   WELCOME TO THE GAME MENU")
    print("="*50)
    print("\n1. Rock - Paper - Scissors")
    print("2. Dice Roll Game")
    print("3. Exit")
    print("-"*50)


def get_menu_choice():
    """Get valid menu choice from user."""
    while True:
        choice = input("Enter your choice (1/2/3): ").strip()
        if choice in ['1', '2', '3']:
            return choice
        print("Invalid choice! Please enter 1, 2, or 3.")


def main():
    """Main function to run the game."""
    print("\n🎮 WELCOME TO THE SIMPLE GAMES 🎮")
    
    while True:
        display_menu()
        choice = get_menu_choice()
        
        if choice == '1':
            play_rock_paper_scissors()
        elif choice == '2':
            play_dice_roll()
        elif choice == '3':
            print("\n👋 Thanks for playing! Goodbye!")
            break
        
        # Ask if player wants to continue
        play_again = input("\nDo you want to play again? (yes/no): ").lower().strip()
        if play_again not in ['yes', 'y']:
            print("\n👋 Thanks for playing! Goodbye!")
            break


if __name__ == "__main__":
    main()
