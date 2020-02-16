import datetime
import time
class LogOpen:
    def __init__(self, path):
        self.path = path
    def __enter__(self):
        self.start = datetime.datetime.now()
        self.file = open(self.path, encoding='utf8')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        self.end = datetime.datetime.now()
        print(f'Время запуска кода:  {self.start}')
        print(f'Время окончания кода: {self.end}')
        print(f'Время работы кода: {self.end - self.start}')

with LogOpen('recipes.txt') as file:
    raw_recipes = file.read()
    list_raw_recipes = raw_recipes.split('\n\n')
    time.sleep(1)
# cook_book = dict()
# for element in list_raw_recipes:
#     data = element.split('\n')
#     cook_book[data[0]] = list()
#     for i in data[2:]:
#         ingridient_name, quantity, measure = i.split(' | ')
#         cook_book[data[0]].append({'ingridient_name':ingridient_name,
#                                    'quantity':int(quantity),
#                                    'measure':measure})
# # for k in cook_book:
# #     print(k, cook_book[k])
#
# def get_shop_list_by_dishes(dishes, person_count):
#     ing = dict()
#     for d in dishes:
#         for i in cook_book[d]:
#             if i['ingridient_name'] in ing:
#                 ing[i['ingridient_name']]['quantity'] += i['quantity'] * person_count
#             else:
#                 ing[i['ingridient_name']] = {'measure': i['measure'],
#                                              'quantity': i['quantity'] * person_count}
#     return ing
#
# result = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
# for i in result.items():
#     print(i)
#
