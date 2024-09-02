def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    words_split = text.split()

    number_of_words = count_words(words_split)
    characters_count = characters_dictionary(text)

    print(text)
    print(number_of_words)
    print(characters_count)
    
def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(words):
    counter = 0
    for word in words:
        counter += 1
    return counter

def characters_dictionary(string):
  
    lowered_string = string.lower()
    dictionary = {}
    for characters in lowered_string:
        if characters in dictionary:
                dictionary[characters] += 1
        else:
            dictionary[characters] = 1
    return dictionary

main()