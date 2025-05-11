from stats import get_num_words

def get_book_text(path):
    with open(path) as f:
        file_contets = f.read()

    return file_contets;

def main():
    boot_text = get_book_text('./books/frankenstein.txt')
    num_words = get_num_words(boot_text)
    print(str(num_words) + ' words found in the document')

main()
