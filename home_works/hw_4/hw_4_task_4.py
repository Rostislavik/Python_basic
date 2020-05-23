'''
4. Реализовать формирование списка, используя функцию range() и возможности генератора. В список должны войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce().
'''

from functools import reduce
lst = [i for i in range(100,1001) if not i%2]
print(lst)

def my_func(prev_el, el):
    # prev_el - предыдущий элемент
    # el - текущий элемент
   return prev_el + el

print('Сумма элементов списка составляет: ', reduce(my_func, lst))