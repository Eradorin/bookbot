from stats import get_word_count
from stats import get_characters
import sys
if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

    

def get_words(book_path):
    with open(book_path) as f:
        return f.read()

def main():
    book_path = sys.argv[1]
    text = get_words(book_path)
    words = get_word_count(text)
    characters = get_characters(text)
    from stats import sorted_characters
    final_characters = sorted_characters(characters)
    try:
        
       # print("---DEBUG: BOOKBOT header printing---")
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {book_path}")
        print("----------- Word Count ----------")
        print(f"Found {words} total words")
        print("--------- Character Count -------")
    except Exception as e:
        print(f"ERROR: {e}")
  #  print("Debug: About to print characters")
    for char in final_characters:
        if char["char"].isalpha():
            print(f"{char['char']}: {char['count']}")
   # print(f"{final_characters} characters in the document sorted most to least")
   # print("Debug: After printing characters")

main()