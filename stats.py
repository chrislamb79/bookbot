def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        words = file_contents.split( )
        num_words = len(words)
        print(f"Found {num_words} total words")