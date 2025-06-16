import sys
from stats import count_words, convertor, count_character_occurences


def get_book_text(file_path: str) -> str:
    with open(file_path, "r") as f:
        return f.read()


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = count_words(text)
    chars = count_character_occurences(text)
    sorted_chars = convertor(chars)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for e in sorted_chars:
        if e["char"].isalpha():
            print(f"{e['char']}: {e['num']}")
    print("============= END ===============")


main()
