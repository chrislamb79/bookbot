def get_book_test(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    print(file_contents)   
    
def main():
    get_book_test("books/frankenstein.txt")

main()