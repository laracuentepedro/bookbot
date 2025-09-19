from stats import count_words, count_chars

def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    book_text = get_book_text('./books/frankenstein.txt')
    print(book_text)
    count_words(book_text)
    chars = count_chars(book_text)
    print(chars)

main()

