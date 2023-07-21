import json
from pprint import pprint
import os

dict_book = []

def best_book(books):

    max = 0

    for i in range(len(books)) :

        if max < books[i]['customerReviewRank'] :

            max = books[i]['customerReviewRank']

    for j in range(len(books)) :

        if max == books[j]['customerReviewRank'] :

            return books[j]['title']
        



        



# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':

    path_dir = r'C:\Users\SSAFY\Downloads\aladin\aladin\data\books'
    file_list = os.listdir(path_dir)
    for i in file_list :

        books_json = open('data/books/'+ i, encoding='utf-8')
        books_list = json.load(books_json)

        dict_book.append(books_list)

    pprint(best_book(dict_book))