# myguitars.py

import csv
from guitar import Guitar

def main():
    # Step 1: Load guitars from file
    guitars = load_guitars("guitars.csv")
    print("All guitars loaded:")
    for guitar in guitars:
        print(guitar)

    # Step 2: Sort and display guitars by year
    guitars.sort()
    print("\nGuitars sorted by year:")
    for guitar in guitars:
        print(guitar)

    # Step 3: Add new guitars from user input
    add_new_guitars(guitars)

    # Step 4: Save updated list of guitars to the file
    save_guitars("guitars.csv", guitars)
    print("New guitars saved to file.")

def load_guitars(filename):
    guitars = []
    with open(filename, "r") as file:
        reader = csv.reader(file)
        for line in reader:
            name, year, cost = line
            guitars.append(Guitar(name, int(year), float(cost)))
    return guitars

def add_new_guitars(guitars):
    print("\nAdd new guitars (leave name blank to finish):")
    while True:
        name = input("Enter guitar name: ")
        if not name:
            break
        year = int(input("Enter guitar year: "))
        cost = float(input("Enter guitar cost: "))
        guitars.append(Guitar(name, year, cost))

def save_guitars(filename, guitars):
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        for guitar in guitars:
            writer.writerow([guitar.name, guitar.year, guitar.cost])

if __name__ == "__main__":
    main()
