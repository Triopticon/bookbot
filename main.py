def get_book_text(path_to_file):
    with open(path_to_file) as f:
        print(f.read())

def main():
    get_book_text("books/frankenstein.txt")

main()
