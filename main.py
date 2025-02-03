def main():
  book_path = "books/frankenstein.txt"
  text = get_book_text(book_path)
  num_words = get_num_words(text)
  total_char_dictionary = get_num_char(text)
  book_report(book_path,num_words,total_char_dictionary)
  
  

def get_num_words(text):
  words = text.split()
  return len(words)
  
def get_book_text(path):
  with open(path) as f:
    return f.read()
  
def get_num_char(text):
  lowercase_text = text.lower()
  temp_dict = {}
  for i in range(len(lowercase_text)):
    if lowercase_text[i] not in temp_dict:
      temp_dict[lowercase_text[i]] = 0
    temp_dict[lowercase_text[i]] += 1
  return temp_dict

def sort_on(dict):
  return dict["total"]

def book_report(path, word_count,dict_total):
  sorted_print = []
  print(f"--- Begin report of {path} ---")
  print(f"{word_count} words found in the document\n")
  for key, value in dict_total.items():
    if key.isalpha():
      sorted_print.append({"letter": key, "total": value})
  sorted_print.sort(reverse=True, key=sort_on)
  for dictionaries in sorted_print:
      print(f"The '{dictionaries["letter"]}' character was found {dictionaries["total"]}  times")
  print(f"--- End report ---")

main()
