import requests
import re

def get_text(url):
    response = requests.get(url)
    return response.text

def count_word_frequencies(text, words_to_count):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)

    words = text.split()
    word_counts = dict()
    for word in words_to_count:
        word_counts[word] = 0

    target_words = set(word.lower() for word in words_to_count)

    for word in words:
        if word in target_words:
            word_counts[word] += 1

    return word_counts


def read_words(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file if line.strip()]


def main():
    words_file = "words.txt"
    url = "https://eng.mipt.ru/why-mipt/"

    words_to_count = read_words(words_file)
    if not words_to_count:
        print("No words to count")
        return

    text = get_text(url)

    print(count_word_frequencies(text, words_to_count))

if __name__ == "__main__":
    main()