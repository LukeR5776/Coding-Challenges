import random

def generate_random_card():
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
    
    suit = random.choice(suits)
    rank = random.choice(ranks)
    
    return f"{rank} of {suit}"

def main():
    deck = []
    
    print("Random Playing Card Generator")
    print("Press Enter to generate a card")
    print("Press 'Q' to view your deck")
    print("Press 'X' to exit")
    print()
    
    while True:
        user_input = input("Press Enter for a card, Q for deck, X to exit: ").strip().upper()
        
        if user_input == "X":
            print("Thanks for playing!")
            break
        elif user_input == "Q":
            if deck:
                print(f"\nYour deck ({len(deck)} cards):")
                for i, card in enumerate(deck, 1):
                    print(f"{i}. {card}")
                print()
            else:
                print("Your deck is empty.\n")
        elif user_input == "":
            card = generate_random_card()
            deck.append(card)
            print(f"Generated: {card}\n")
        else:
            print("Invalid input. Press Enter, Q, or X.\n")

if __name__ == "__main__":
    main()