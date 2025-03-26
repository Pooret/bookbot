
def num_words_in_text(text):
    return len(text.split())


def num_chars_in_text(text):
    chars = {}
    for char in text.lower():
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return chars


def sort_dict(my_dict):
    return dict([(key,val) for key, val in sorted(my_dict.items(), key=lambda item: item[1], reverse=True) if key.isalpha()])