
my_string = "Hello, my name is Keaton."

# Entry Point Function

def main():
    # reading book file
    book_file_path = "books/frankenstein.txt"
    text = read_books(book_file_path)

    # Count Words
    word_count = get_word_count(text)

    # Character Count
        # Convert to Lower Case
    character_dict = get_character_count(text)
    print(character_dict)

    # Print Report
        # Word and char data
    # print_report(book_file_path, word_count, charcter_dict)


def read_books(path):
    with open(path) as f:
        return f.read()


def get_word_count(book_text):
    words = book_text.split()
    count_words = len(words)
    return count_words


def get_character_count(string):
    char_count_dict = {}
    lower_case_string = string.lower()
    
    for words in lower_case_string:
        word = words.split()

        for char in word:
            if char in char_count_dict:
                char_count_dict[char] += 1
            else:
                char_count_dict[char] = 1
    return char_count_dict                     





main()

# python3 main.py