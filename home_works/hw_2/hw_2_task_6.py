'''
6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
Каждый кортеж хранит информацию об отдельном товаре.
В кортеже должно быть два элемента — номер товара и словарь с параметрами (характеристиками товара: название, цена, количество, единица измерения).
Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
'''

goods = []
features = {'наименование': '', 'цена': '', 'количество': '', 'ед.изм': ''}
analytics = {'наименование': [], 'цена': [], 'количество': [], 'ед.изм': []}
num = 0
feature_ = None
control = None
while True:
    control = input("Для выхода жми '1', Для продолжения жми 'Enter', Для анализа жми '2'").upper()
    if control == '1':
        break
    num += 1
    if control == '2':
        print(f'\n АНАЛИЗ: \n {"-" * 30}')
        for key, value in analytics.items():
            print(key, value)
            print("-" * 30)
        break
    for f in features.keys():
        feature_ = input(f'Введи "{f}"')
        features[f] = int(feature_) if (f == 'цена' or f == 'количество') else feature_
        analytics[f].append(features[f])
    goods.append((num, features))
