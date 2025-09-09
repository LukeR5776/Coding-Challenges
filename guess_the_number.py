import random

def human_guesses():
    """Mode where human guesses the computer's number"""
    print("\n🎯 HUMAN GUESSING MODE")
    print("I'm thinking of a number between 1 and 100...")
    
    # Computer picks random number
    secret_number = random.randint(1, 100)
    attempts = 0
    
    while True:
        try:
            # Get user's guess
            guess = int(input("\nEnter your guess (1-100): "))
            attempts += 1
            
            # Validate input range
            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100!")
                attempts -= 1  # Don't count invalid attempts
                continue
            
            # Check the guess
            if guess == secret_number:
                print(f"🎉 You got it! The number was {secret_number}")
                print(f"It took you {attempts} attempts!")
                break
            elif guess < secret_number:
                print("📈 Too low!")
            else:
                print("📉 Too high!")
                
        except ValueError:
            print("Please enter a valid number!")
            attempts -= 1  # Don't count invalid attempts

def computer_guesses():
    """Mode where computer guesses the human's number"""
    print("\n🤖 COMPUTER GUESSING MODE")
    print("Think of a number between 1 and 100, and I'll try to guess it!")
    print("Respond with: (C)orrect, (H)igh if my guess is too high, or (L)ow if my guess is too low")
    
    input("\nPress Enter when you have a number in mind...")
    
    # Computer uses binary search strategy
    low = 1
    high = 100
    attempts = 0
    
    while True:
        attempts += 1
        
        # Computer's guess (binary search)
        guess = (low + high) // 2
        
        print(f"\nAttempt {attempts}: Is your number {guess}?")
        response = input("Enter (C)orrect, (H)igh, or (L)ow: ").upper().strip()
        
        if response == 'C' or response == 'CORRECT':
            print(f"🎉 I got it! Your number was {guess}")
            print(f"It took me {attempts} attempts!")
            break
        elif response == 'H' or response == 'HIGH':
            high = guess - 1
            print("Got it, your number is lower than that.")
        elif response == 'L' or response == 'LOW':
            low = guess + 1
            print("Got it, your number is higher than that.")
        else:
            print("Please enter 'C' for correct, 'H' for high, or 'L' for low.")
            attempts -= 1  # Don't count invalid responses
            continue
        
        # Check if the range is impossible
        if low > high:
            print("🤔 Hmm, it seems like there might be an inconsistency in your responses.")
            print("Let's start over!")
            return computer_guesses()

def display_menu():
    """Display the main menu"""
    print("\n" + "="*50)
    print("🎮 GUESS THE NUMBER GAME")
    print("="*50)
    print("Choose your game mode:")
    print("1. I guess your number (Human guesses)")
    print("2. You guess my number (Computer guesses)")
    print("3. Exit game")
    print("="*50)

def get_user_choice():
    """Get and validate user's menu choice"""
    while True:
        try:
            choice = int(input("\nEnter your choice (1-3): "))
            if choice in [1, 2, 3]:
                return choice
            else:
                print("Please enter 1, 2, or 3!")
        except ValueError:
            print("Please enter a valid number!")

def play_again():
    """Ask if user wants to play again"""
    while True:
        response = input("\nWould you like to play again? (y/n): ").lower().strip()
        if response in ['y', 'yes']:
            return True
        elif response in ['n', 'no']:
            return False
        else:
            print("Please enter 'y' for yes or 'n' for no.")

def main():
    """Main game loop"""
    print("Welcome to the Guess The Number Game! 🎲")
    
    while True:
        display_menu()
        choice = get_user_choice()
        
        if choice == 1:
            human_guesses()
        elif choice == 2:
            computer_guesses()
        elif choice == 3:
            print("\nThanks for playing! Goodbye! 👋")
            break
        
        if not play_again():
            print("\nThanks for playing! Goodbye! 👋")
            break

if __name__ == "__main__":
    main()