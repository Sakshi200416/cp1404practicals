from prac_06.guitar import Guitar

def main():
    guitars = []
    print("My guitars!")

    while True:
        name = input("Name: ")
        if not name:
            break
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        new_guitar = Guitar(name, year, cost)
        guitars.append(new_guitar)
        print(f"{new_guitar} added.\n")

    print("\nThese are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = "(vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar} {vintage_string}")

if __name__ == "__main__":
    main()
