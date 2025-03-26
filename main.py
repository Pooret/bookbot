
from stats import num_words_in_text, num_chars_in_text, sort_dict
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        return str(f.read())


def main():
    print("============ BOOKBOT ============")
    if len(sys.argv) !=2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book = sys.argv[-1]
    contents = get_book_text(book)
    print("Analyzing book found at books/frankenstein.txt...")
    num_words = num_words_in_text(contents)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    num_chars = num_chars_in_text(contents)
    num_chars_sorted = sort_dict(num_chars)
    for key, val in num_chars_sorted.items():
        print(f"{key}: {val}")


main()