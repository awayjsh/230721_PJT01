import json
from pprint import pprint



def sorted_cs_books_by_price(books, categories):

    ans = []
    computer = []
    final_lst = []

    for i in range(len(books)) :

        part_books = {}
        categories_lst = []

        part_books['author'] = books[i]['author']
        part_books['cover'] = books[i]['cover']
        part_books['description'] = books[i]['description']
        part_books['id'] = books[i]['id']
        part_books['priceSales'] = books[i]['priceSales']
        part_books['title'] = books[i]['title']

        for j in range(len(categories)) :

            if categories[j]['id'] in books[i]['categoryId'] :

                categories_lst.append(categories[j]['name'])
            
        part_books['categoryId'] = categories_lst


        ans.append(part_books)

    for i in range(len(ans)) :

        if '컴퓨터 공학' in ans[i]['categoryId'] :

            computer.append(ans[i]['priceSales'])

    computer.sort(reverse = True)

    for i in computer :

        for j in range(len(books)) :

            if i == books[j]['priceSales'] :

                final_lst.append(books[j]['title'])

    return final_lst


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    books_json = open('data/books.json', encoding='utf-8')
    books = json.load(books_json)

    categories_json = open('data/categories.json', encoding='utf-8')
    categories_list = json.load(categories_json)

    print(sorted_cs_books_by_price(books, categories_list))
