def get_num_words(text_to_count):
    words = text_to_count.split()
    word_count = len(words)

    return word_count

def count_characters(text_to_count):
    characters = {}

    for char in text_to_count.lower():
        if char.isalpha():
            if char not in characters:
                characters[char] = 0
            characters[char] += 1

    return characters

def get_sorted_char_counts(char_counts):
    # Convert the dictionary to a list of dicts
    char_list = [{"char": char, "num": count} for char, count in char_counts.items()]
    # Sort the list in descending order by count
    char_list.sort(key=lambda item: item["num"], reverse=True)

    return char_list
