import json
from pprint import pprint


def book_info(book,categories):
    
    ans = {}
    categories_lst = []

    ans['author'] = book['author']
    ans['cover'] = book['cover']
    ans['description'] = book['description']
    ans['id'] = book['id']
    ans['priceSales'] = book['priceSales']
    ans['title'] = book['title']

    for i in range(len(categories)) :

        if categories[i]['id'] in book['categoryId'] :

            categories_lst.append(categories[i]['name'])

    ans['categoryName'] = categories_lst
    

    return ans

        


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    book_json = open('data/book.json', encoding='utf-8')
    book = json.load(book_json)

    categories_json = open('data/categories.json', encoding='utf-8')
    categories_list = json.load(categories_json)

    pprint(book_info(book,categories_list))
