
book_title = "books/frankenstein.txt"

with open(book_title) as f:
        file_contents = f.read()


def count_words():
    words = file_contents.split()
    return(len(words))

def sort_on(dict):
    return dict["num"]

def count_characters(file_contents):
    char_count = {}
    char_list = []
    lower_case_words = file_contents.lower()

    for char in lower_case_words:
        if char.isalpha():
            if char in char_count: 
                char_count[char] += 1
            else: 
                char_count[char] = 1

    for char, count in char_count.items():
        char_dict = {"char" : char, "num": count}
        char_list.append(char_dict)
        
    char_list.sort(reverse=True, key=sort_on)

    return (char_list)


print(f"--- Begin report of {book_title} ---")
print(f"{count_words()} words found in the document")

char_counts = count_characters(file_contents)
for char_dict in char_counts:
    print(f"The '{char_dict['char']}' character was found {char_dict['num']} times")
