def extract_name(email):

    name_part = email.split('@')[0]
    name = name_part.replace('.', ' ').title()
    return name


def main():

    user_data = {}

    while True:
        email = input("Email: ").strip()
        if not email:
            break

        name = extract_name(email)
        confirmation = input(f"Is your name {name}? (Y/n) ").strip().lower()

        if confirmation not in ('', 'y'):  # If not Yes (default) or Y, ask for name
            name = input("Name: ").strip()

        user_data[email] = name  # Store email and name in the dictionary

    # Print all emails and names
    for email, name in user_data.items():
        print(f"{name} ({email})")


# Run
main()
