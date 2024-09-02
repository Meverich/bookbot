def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    words_split = text.split()

    number_of_words = count_words(words_split)
    characters_count = characters_dictionary(text)
    letter_value = dictionaries_listed(characters_count)
    letter_value.sort(reverse=True, key=sort_on)
    # This should sort the list of characters

    print ("--- Begin report of books/frankenstein.txt ---")
    print(number_of_words, "words found in the document")
    print()
    # This prints the number of words
    print_list(letter_value)
    print("--- End report ---")
    
def get_book_text(path):
    with open(path) as f:
        return f.read()
# This opens the txt. file

def count_words(words):
    counter = 0
    for word in words:
        counter += 1
    return counter
# This counts the words

def characters_dictionary(string):
    lowered_string = string.lower()
    dictionary = {}
    for characters in lowered_string:
        if characters in dictionary:
                dictionary[characters] += 1
        elif characters.isalpha() == True:
            dictionary[characters] = 1
    return dictionary
# This returns the dictionary with the numbers of all the characters excluding symbols not in the alphabet

def dictionaries_listed(characters_count):
    dictionaries_list = []
    for letter, count in characters_count.items():
        temporary_dictionary = {"letter": letter, "num": count}
        dictionaries_list.append(temporary_dictionary)
    return dictionaries_list
# This returns a list of all the dictionaries with letter/num pairs

def sort_on(letter_value):
    return letter_value["num"]

def print_list(letter_value):
    for dict in letter_value:
        print(f"The '{dict['letter']}' character was found {dict['num']} times")
main()