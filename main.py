
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


    # Print Report
        # Word and char data
    # print_report(book_file_path, word_count, charcter_dict)
    chars_sorted_list = chars_dict_to_sorted_list(character_dict)

    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")

    

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


# Converting a dictionary into a list of dictionaries
def sort_on(dict):
    return dict["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []

    for char in num_chars_dict:
        sorted_list.append({"char": char, "num": num_chars_dict[char]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list




main()

# python3 main.py