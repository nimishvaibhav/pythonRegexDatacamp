import re
import requests


# def get_book(book_url):
    # raw = requests.get(book_url).text

def get_book_data():
    with open('The_Idiot.txt', 'r', encoding='utf-8') as f:
        book = f.read()
    return book


def finding_part(book):
    # pattern = re.compile(r'(PART\s+(I|II|III|IV))')
    pattern = re.compile(r'PART\s(I|II|V)+')
    matches = pattern.finditer(book)
    print(matches)

    for match in matches:
        print(match)


if __name__ == '__main__':
    # the_idiot_url = 'https://www.gutenberg.org/files/2638/2638-0.txt'
    # get_book(the_idiot_url)
    get_book_data()
    finding_part(get_book_data())



