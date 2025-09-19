from stats import count_words

def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    book_text = get_book_text('./books/frankenstein.txt')
    print(book_text)
    count_words(book_text)

main()

