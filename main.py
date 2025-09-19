from stats import count_words, count_chars, create_report
import sys

def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    if len(sys.argv) < 2:
        print("Looks like you're missing an argument!")
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_text = get_book_text(sys.argv[1])
    print(book_text)
    words = count_words(book_text)
    chars = count_chars(book_text)
    print(chars)
    report = create_report(chars)
    print(f"============ BOOKBOT ============\nAnalyzing book found at {sys.argv[1]}...\n----------- Word Count -----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")
    for entry in report:
        if entry["char"].isalpha():
             print(f"{entry["char"]}: {entry["num"]}")
    print("============= END ===============")


main()

