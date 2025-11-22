def get_num_words(book_text):
    word_count = len(book_text.split())
    print(f"Found {word_count} total words")

def character_count(book_text):
    character_list = list(book_text.lower())
    character_count_dictionary = {}
    for character in character_list:
        if character in character_count_dictionary:
            character_count_dictionary[character] += 1
        else:
            character_count_dictionary[character] = 1
    sorted_dict = sorted(character_count_dictionary.items(), key=lambda item: item[1], reverse = True)
    for letter, number in sorted_dict:
        if letter.isalpha():
            print(f"{letter}: {number}")
        

