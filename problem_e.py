import json
from pprint import pprint
import os

dict_book = []


def new_books(books):

    ans = []

    for i in range(len(books)) :

        if int(books[i]['pubDate'][0:4]) == 2023 :

            ans.append(books[i]['title'])

    return ans



# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':

    path_dir = r'C:\Users\SSAFY\Downloads\aladin\aladin\data\books'
    file_list = os.listdir(path_dir)
    for i in file_list :

        books_json = open('data/books/'+ i, encoding='utf-8')
        books_list = json.load(books_json)

        dict_book.append(books_list)
    
    print(new_books(dict_book))
