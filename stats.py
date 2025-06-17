def word_count(full_text):
    word_list = full_text.split()
    return len(word_list)

def get_char_dict(book_string):
    
    file_contents = book_string.lower()
    char_dict = {}
    for char in file_contents:
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1
        
    return char_dict

def sort_on(dict):
    return dict["num"]

def dict_sort(char_dict):
    details_list = []
    for char in char_dict:
        if char.isalpha():
            tmp_dict = {"char":char,"num":char_dict[char]}
            details_list.append(tmp_dict)
    details_list.sort(reverse=True, key=sort_on)
    return details_list