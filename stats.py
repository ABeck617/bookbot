def get_num_words(text):
    words = text.split()
    return len(words)
    # with open("books/frankenstein.txt") as file:
    #     file_contents = file.read()
    #     num_words = file_contents.split()
    #     letter_list = list(file_contents)

    #     characters = {}

    #     for letter in letter_list:
    #         if letter.isalpha() != True:
    #             continue

    #     for letter in letter_list:
    #         lowercase_letter = letter.lower()
    #         if lowercase_letter in characters:
    #             characters[lowercase_letter] = characters[lowercase_letter] + 1
    #         else:
    #             characters[lowercase_letter] = 1


    #     # print("--- Begin report of books/frankenstein.txt ---")
    #     # for character in characters:
    #     #     print((f"{character}: {characters[character]}"))
    #     # print("--- End report ---")
                
    #     print("--- Begin report of books/frankenstein.txt ---")
    #     for character, count in sorted(characters.items(), key=lambda item: item[1], reverse=True):
    #         print(f"{character}: {count}")
    #     print("--- End report ---")

        
    # print("============ BOOKBOT ============")
    # print("Analyzing book found at books/frankenstein.txt...")

    # with open("books/frankenstein.txt") as file:
    #     file_contents = file.read()

    # # Count total words
    # words = file_contents.split()
    # total_words = len(words)

    # # Count characters
    # characters = {}
    # for letter in file_contents:
    #     if letter.isalpha():
    #         lowercase_letter = letter.lower()
    #         if lowercase_letter in characters:
    #             characters[lowercase_letter] += 1
    #         else:
    #             characters[lowercase_letter] = 1

    # print("----------- Word Count ----------")
    # print(f"Found {total_words} total words")

    # print("--------- Character Count -------")
    # for char, count in sorted(characters.items(), key=lambda item: item[1], reverse=True):
    #     print(f"{char}: {count}")

    # print("============= END ===============")

    

