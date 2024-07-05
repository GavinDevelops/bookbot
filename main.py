def get_num_words(text):
    return len(text.split())

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_chars(text):
    d = {}

    text = text.lower()
    for char in text:
        if char in d:
            d[char] += 1
        elif char.isalpha():
            d[char] = 1
    return d 

def convert_dict_to_list(d):
    l = []
    for k in d:
        l.append({"char": k, "num": d[k]})
    return l
    
def sort_list_dict(d):
    return d["num"]

def print_report(book_path):
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_num_chars(text)
    chars_list = convert_dict_to_list(chars_dict)
    chars_list.sort(reverse=True, key=sort_list_dict)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document\n")
    for i in chars_list:
        print(f"The '{i["char"]}' character was found {i["num"]} times")
    print("--- End report ---")

def main():
    book_path = "./books/frankenstein.txt"
    print_report(book_path)

main()
