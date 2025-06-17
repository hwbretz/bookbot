import sys
from stats import word_count
from stats import get_char_dict
from stats import dict_sort

def get_book_text(path_to_file):
    with open(path_to_file) as book_file:
        file_contents = book_file.read()
        return file_contents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    text = get_book_text(file_path)
    count = word_count(text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    char_dict_list = dict_sort(get_char_dict(text))
    for dict in char_dict_list:
        print(f"{dict["char"]}: {dict["num"]}")


main()
