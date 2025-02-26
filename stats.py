def get_word_count(text):
    words = text.split()
    return len(words)

def get_characters(text):
    characters = {}
    for char in text.lower():
        if char in characters:
            characters[char] +=1
        else:
            characters[char] = 1
    
    return characters

def sorted_characters(characters):

    char_list = [
        {"char": key, "count": value} for key, value in characters.items() if key.isalpha()
    ]
    char_list.sort(reverse=True, key=lambda item: item["count"])

    return char_list
