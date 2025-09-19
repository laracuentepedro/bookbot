def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    num_words = len(text.split())
    print(f"{num_words} words found in the document")
    return num_words
def main():
    book_text = get_book_text('./books/frankenstein.txt')
    print(book_text)
    count_words(book_text)

main()

