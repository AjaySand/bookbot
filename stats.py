def get_num_words(text):
    return len(text.split())

def char_occurrences(text):
    text = text.lower()
    occurrences = {}
    for char in text:
        occurrences[char] = occurrences.get(char, 0) + 1

    occurrences = dict(sorted(occurrences.items(), key=lambda x: x[1], reverse=True))
    return occurrences
