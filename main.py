import sys
from stats import get_num_words  # Assumes you have get_num_words in stats.py

def main():
    # Check if the book path was provided
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    
    # Read the book and perform analysis
    text = read_book(book_path)
    words = get_num_words(text)
    letters = letter_count(text)
    letters_list = dict_to_list(letters)
    letters_list.sort(reverse=True, key=sort_on)

    # Output
    print(f"""============ BOOKBOT ============
Analyzing book found at {book_path}...
----------- Word Count ----------
Found {words} total words
--------- Character Count -------""")

    for item in letters_list:
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")

# Sort helper
def sort_on(d):
    return d["num"]

# Convert dictionary to list of dicts for sorting
def dict_to_list(letters):
    dict_letters = []
    for letter in letters:
        if letter.isalpha():  # Skip punctuation, numbers, etc.
            dict_letters.append({"char": letter, "num": letters[letter]})
    return dict_letters

# Reads the text file and returns the full string
def read_book(path):
    with open(path, encoding="utf8") as f:  # utf8 helps with special characters
        return f.read()

# Count characters in the book text
def letter_count(text):
    text_lower = text.lower()
    letters = {}
    for char in text_lower:
        if char in letters:
            letters[char] += 1
        else:
            letters[char] = 1
    return letters

# Start the program
if __name__ == "__main__":
    main()

# def main():
#     with open("books/frankenstein.txt") as file:
#         file_contents = file.read()
#         num_words = file_contents.split()
#         result = str(len(num_words)) + " words found in the document"

#         print(result)

# main()
