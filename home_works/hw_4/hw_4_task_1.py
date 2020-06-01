'''
1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
'''

import sys
from sys import argv

name_file, time, salary, bonus = argv
_, *vars = sys.argv
tmp = [itm for itm in vars if itm.isdigit()]
print(tmp)
res = float(tmp[0])*float(tmp[1])+float(tmp[2])
print(f'Заработная плата сотрудника:  {res}')