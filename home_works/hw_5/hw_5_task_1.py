'''
1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
'''

fname = input('Файл: ')
f = open(fname,'w', encoding='utf-8')
while True:
    s = input()
    if s == '': break
    f.write(s+'\n')
f.close()