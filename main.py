def get_book_text(filepath):
    with open(filepath) as f:
        text = f.read()
    print(text)

def main():
    get_book_text(chris/bookbot/books/frankenstein.txt)

if __name__ == "__main__":
    main()