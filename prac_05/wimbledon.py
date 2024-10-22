def read_data(filename):
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        # Skip the header line
        next(in_file)
        data = [line.strip().split(',') for line in in_file]
    return data


def count_champions(data):
    """Count how many times each champion has won."""
    champions = {}
    for row in data:
        champion = row[2]
        if champion in champions:
            champions[champion] += 1
        else:
            champions[champion] = 1
    return champions


def get_countries(data):
    """Get a set of unique countries of the champions."""
    countries = set()
    for row in data:
        country = row[1]  # Country of the champion
        countries.add(country)
    return countries


def main():
    """Main function to process Wimbledon display results."""
    filename = 'prac_05/wimbledon.csv'
    data = read_data(filename)

    champions = count_champions(data)

    print("Wimbledon Champions: ")
    for champion, count in sorted(champions.items(), key=lambda x: x[0]):
        print(f"{champion} {count}")

    countries = get_countries(data)
    sorted_countries = sorted(countries)
    print("\nThese countries have won Wimbledon: ")
    print(", ".join(sorted_countries))


# Run
if __name__ == "__main__":
    main()
