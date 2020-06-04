"""
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""

replace = {'One — 1': 'Один — 1', 'Two — 2': 'Два — 2', 'Three — 3': 'Три — 3', 'Four — 4': 'Четыре — 4'}
with open('text_file_2.txt','r', encoding="utf-8") as f_in, open('text_file_3.txt', 'w', encoding="utf-8") as f_out:
    for line in f_in:
        for key, value in replace.items():
            line = line.replace(key, value)
        f_out.write(line)
