

def main():
    path_to_file = "books/frankenstein.txt"

    with open(path_to_file) as f:
        file_contents = f.read()
        # print(file_contents)
        word_count = string_to_words(file_contents)
        letters = string_to_letter_count(file_contents)
        print_book_report(path_to_file, word_count, letters)
    


def string_to_words(string):
    return len(string.split())

def string_to_letter_count(string):
    letters = {}

    for char in string.lower():
        if not char.isalpha():
            continue
        if not char in letters:
            letters[char] = 1
            continue
        letters[char] += 1
    return letters

def print_book_report(file_path, word_count, letters):
    print(f"--- Begin the report of {file_path} ---")
    print(f"{word_count} words found in the document")
    print()
    for letter in letters:
        print(f"The '{letter}' character was found {letters[letter]} times")

    print("--- End report ---")

main()
