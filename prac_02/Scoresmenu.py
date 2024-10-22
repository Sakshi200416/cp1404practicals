def main():
    print("Welcome to the Score Menu Program!")
    score = get_valid_score()

    while True:
        display_menu()
        choice = input("Choose an option: ").upper()

        if choice == 'G':
            score = get_valid_score()
        elif choice == 'P':
            print(f"Result: {determine_status(score)}")
        elif choice == 'S':
            show_stars(score)
        elif choice == 'Q':
            print("Farewell!")
            break
        else:
            print("Invalid choice, please select again.")


def display_menu():
    """Display the menu options."""
    print("\nMenu:")
    print("(G)et a valid score")
    print("(P)rint result")
    print("(S)how stars")
    print("(Q)uit")


def get_valid_score():
    """Get a valid score between 0 and 100 inclusive."""
    while True:
        try:
            score = float(input("Enter a valid score (0-100): "))
            if 0 <= score <= 100:
                return score
            else:
                print("Invalid score, must be between 0 and 100.")
        except ValueError:
            print("Invalid input, please enter a number.")


def determine_status(score):
    """Determine the status of the score."""
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def show_stars(score):
    """Print as many stars as the score."""
    print('*' * int(score))


# Start the program
main()
