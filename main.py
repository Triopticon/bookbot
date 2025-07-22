import sys
from stats import get_num_words
from stats import count_characters
from stats import get_sorted_char_counts

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_path = sys.argv[1]
    file_contents = get_book_text(book_path)
    num_words = get_num_words(file_contents)
    char_count = count_characters(file_contents)
    sorted_char_counts = get_sorted_char_counts(char_count)
    print_report(book_path, num_words, sorted_char_counts)

    
def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()

    return file_contents

def print_report(book_path, num_words, sorted_char_counts):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char in sorted_char_counts:
        print(f"{char['char']}: {char['num']}")
    print("============= END ===============")


main()
