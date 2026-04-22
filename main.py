"""Main Game Menu"""

from games import rock_paper_scissors


def display_menu():
    """Display the main menu."""
    print("\n" + "="*50)
    print("   WELCOME TO THE GAME MENU")
    print("="*50)
    print("\n1. Rock - Paper - Scissors")
    print("2. Exit")
    print("-"*50)


def get_menu_choice():
    """Get valid menu choice from user."""
    while True:
        choice = input("Enter your choice (1/2): ").strip()
        if choice in ['1', '2']:
            return choice
print("Invalid choice! Please enter 1 or 2.")


def main():
    """Main function - runs the game menu."""
    print("\n🎮 WELCOME TO THE SIMPLE GAMES 🎮")
    
    while True:
        display_menu()
        choice = get_menu_choice()
        
        if choice == '1':
            rock_paper_scissors.play()
        elif choice == '2':
            print("\n👋 Thanks for playing! Goodbye!")
            break
        
        play_again = input("\nDo you want to play again? (yes/no): ").lower().strip()
        if play_again not in ['yes', 'y']:
            print("\n👋 Thanks for playing! Goodbye!")
            break


if __name__ == "__main__":
    main()
