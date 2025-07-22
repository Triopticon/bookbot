def main():
    file_contents = get_book_text("books/frankenstein.txt")
    num_words = count_words(file_contents)
    print(f"{num_words} words found in the document")

    
def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()

    return file_contents

def count_words(text_to_count):
    words = text_to_count.split()
    word_count = len(words)

    return word_count

main()
