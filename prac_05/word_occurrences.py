def count_word_occurrences():
    # Ask the user for input
    text = input("Text: ")

    # Split the text into words and count occurrences
    word_count = {}
    for word in text.split():
        word_count[word] = word_count.get(word, 0) + 1

    sorted_words = sorted(word_count)

    # Print the results
    longest_word_length = max(len(word) for word in sorted_words)
    for word in sorted_words:
        print(f"{word:<{longest_word_length}} : {word_count[word]}")


# Run the program
count_word_occurrences()
if __name__ == '__main__':
    count_word_occurrences()
