"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""
from statistics import mean
with open('text_file_5.txt','r', encoding="utf-8") as f:
    workers = {}
    for line in f:
        key, value = line.split(" ")
        workers[key] = value
        if int(value) < 20000:
            print(f'{key}: зарплата меньше 20000')
    a = mean(int(workers[k]) for k in workers)
    print('Средняя заработная плата сотрудников составляет:', a)