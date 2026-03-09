def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        words = file_contents.split( )
        num_words = len(words)
        print(f"Found {num_words} total words")

def char_count(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        file_contents = file_contents.lower()
        char_list = [
            "a",
            "b",
            "c",
            "d",
            "e",
            "f",
            "g",
            "h",
            "i",
            "j",
            "k",
            "l",
            "m",
            "n",
            "o",
            "p",
            "q",
            "r",
            "s",
            "t",
            "u",
            "v",
            "w",
            "x",
            "y",
            "z",
            " ",
            ]
        for i in char_list:
            file_contents.count(i)
            count_dict={
                "letter":i,
                "count": file_contents.count(i)
            }
            # print(f"Number of times {i} appears = {file_contents.count(i)}")
            print(f"'{count_dict["letter"]}': {count_dict["count"]}")
