def count_num_words(text):
    words = text.split()
    return len(words)

def get_chars_dict(text):
    chars = {}
    for t in text:
        lowered = t.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


