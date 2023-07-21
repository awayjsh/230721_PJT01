import json
from pprint import pprint



def book_info(book):
    
    ans = {}

    ans['author'] = book['author']
    ans['categoryId'] = book['categoryId']
    ans['cover'] = book['cover']
    ans['description'] = book['description']
    ans['id'] = book['id']
    ans['priceSales'] = book['priceSales']
    ans['title'] = book['title']
    

    return ans




# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    book_json = open('data/book.json', encoding='utf-8')
    book = json.load(book_json)
    
    pprint(book_info(book))
