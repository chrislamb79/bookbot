def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def count_num_words(text):
    words = text.split()
    print("******** file output with split command ***************")
    print(len(words))
    print("******** file output with split command ***************")


def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print("********* raw file output *****************")
    print(text)
    print("********* raw file output *****************")
    text_after_split = text.split()
    print("********* text after split *****************")
    print(text_after_split)
    print("********* text after split *****************")



main()