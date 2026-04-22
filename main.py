"""Main Game Menu - Calls different game modules"""

from games import rock_paper_scissors, dice_roll


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
    """Main function to run the game menu and call game functions."""
    print("\n🎮 WELCOME TO THE SIMPLE GAMES 🎮")
    
    while True:
        display_menu()
        choice = get_menu_choice()
        
        if choice == '1':
            # Call rock-paper-scissors game function
            rock_paper_scissors.play()
        elif choice == '2':
            # Call dice roll game function
            dice_roll.play()
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
