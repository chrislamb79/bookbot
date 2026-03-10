from stats import count_num_words, get_chars_dict

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = count_num_words(text)
    chars_dict = get_chars_dict(text)
    print(f"Found {num_words} total words")
    print(chars_dict)

main()