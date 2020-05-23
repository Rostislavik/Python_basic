'''
6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
Каждое слово состоит из латинских букв в нижнем регистре.
Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
Необходимо использовать написанную ранее функцию int_func().
'''


def cap(word):
   first_letter_small = word[0]
   first_letter_big = chr(ord(first_letter_small) - ord('a') + ord('A'))
   return first_letter_big + word[1:]

source = input('Введите слово строчными буквами: \n').split()
res = []
for word in source:
    res.append(cap(word))
print(' '.join(res))

source_1 = input('Отлично, а теперь введите строчными буквами несколько слов через пробел: \n').split()
res = []
for word in source_1:
    res.append(cap(word))
print(' '.join(res))