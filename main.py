from stats import char_occurrences, get_num_words

def get_book_text(path):
    with open(path) as f:
        file_contets = f.read()

    return file_contets;

def main():
    file_path = "books/frankenstein.txt"
    print("============ BOOKBOT ============")
    print("Analyzing book found at " + file_path + "...")
    book_text = get_book_text(file_path)

    print("----------- Word Count ----------")
    word_count = get_num_words(book_text)
    print("Found " + str(word_count) + " total words")

    print("--------- Character Count -------")
    occurences = char_occurrences(book_text)

    for char, count in occurences.items():
        if char.isalpha():
            print(f"{char}: {count}")

    print("============= END ===============")
main()
