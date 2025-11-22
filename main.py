from stats import get_num_words, character_count
import sys

def get_book_text(file):
    get_num_words(file)
    character_count(file)

def main():
    if len(sys.argv) > 1:
        with open(sys.argv[1]) as f:
            file_path = f.read()
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    get_book_text(file_path)

if __name__ == "__main__":
    main()
