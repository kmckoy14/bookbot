
# Entry Point Function

def main():
    # reading book file
    book_file_path = "books/frankenstein.txt"
    text = read_books(book_file_path)

    # Count Words
    word_count = get_word_count(text)
    

def get_word_count(book_text):
    words = book_text.split()
    count_words = len(words)
    return count_words



def read_books(path):
    with open(path) as f:
        return f.read()


main()
# python3 main.py