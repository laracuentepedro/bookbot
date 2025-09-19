def count_words(text):
    num_words = len(text.split())
    print(f"{num_words} words found in the document")
    return num_words

def count_chars(text):
    store = {}
    for char in text:
        normalized_char = char.lower()
        if normalized_char not in store:
            store[normalized_char] = 0
        store[normalized_char] += 1
    return store