from stats import count_words, count_chars, create_report

def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    book_text = get_book_text('./books/frankenstein.txt')
    print(book_text)
    words = count_words(book_text)
    chars = count_chars(book_text)
    print(chars)
    report = create_report(chars)
    print("============ BOOKBOT ============\nAnalyzing book found at books/frankenstein.txt...\n----------- Word Count -----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")
    for entry in report:
        if entry["char"].isalpha():
             print(f"{entry["char"]}: {entry["num"]}")
    print("============= END ===============")


main()

