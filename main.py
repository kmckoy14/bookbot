
# Entry Point Function

def main():
    # reading book file
    book_file_path = "books/frankenstein.txt"
    read = read_books(book_file_path)
    print(read)

def read_books(path):
    with open(path) as f:
        return f.read()


main()
# python3 main.py