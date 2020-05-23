'Соловьев С.Н. Домашняя работа 1'

print('task_1')
'''1. Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя несколько чисел и строк
и сохраните в переменные, выведите на экран.'''
a = 100
print(a)

b = 'hello word!'
print(b)

a = input('Введите число \n')
int(a)
print(a)

a = input('Введите слово\n')
str(a)
print(a)

print("-" * 50)
print('task_2')
'''2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.'''

a = input('Введите произвольное количество секунд \n')
if a.isdigit():
    a = int(a)
    h = str(a // 3600)
    m = (a // 60) % 60
    s = a % 60
    if m < 10:
        m = '0'+str(m)
    else:
        m = str(m)
    if s < 10:
        s = '0'+str(s)
    else:
        s = str(s)
print('Это соответствует: '+h+':'+m+':'+s)

print("-" * 50)
print('task_3')
'''3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.'''

n = input('Введите любое число \n')
if n.isdigit():
    n = int(n)
    temp = str(n)
    t1 = temp + temp
    t2 = temp + temp + temp
    comp = n + int(t1) + int(t2)
    print("Результат:",comp)
else:
    print('Вы ввели не число... Прощайте!')

print("-" * 50)
print('task_4')
'''4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.'''

a = input('Введите двузначное или многозначное целое положительное число \n')
a = int(a)
r = -1
if a > 10:
    while a > 10:
        d = a % 10
        a //= 10
        if d > r:
            r = d
        print(r)
else:
    print('Вы ввели некорректное число')


'''5. Запросите у пользователя значения выручки и издержек фирмы.
Определите, с каким финансовым результатом работает фирма (прибыль — выручка больше издержек, 
или убыток — издержки больше выручки). Выведите соответствующее сообщение. Если фирма отработала с прибылью, 
вычислите рентабельность выручки (соотношение прибыли к выручке). Далее запросите численность сотрудников фирмы 
и определите прибыль фирмы в расчете на одного сотрудника.'''
print("-" * 50)
print('task_5')
revenue = input('Введите размер годовой выручки Вашей Компании (тыс. руб.):\n')
cost = input('Введите размер годовых издержек Вашей Компании(тыс. руб.):\n')
revenue = int(revenue)
cost = int(cost)
comp_1 = revenue - cost
comp_2 = comp_1 / cost * 100
if comp_1 > 0:
    print('Ваша Компания имеет годовую прибыль:',comp_1, 'тыс.р.', 'Рентабельность составила:', round(comp_2,2), '% годовых')
    staff = input('Введите среднегодовое количество сотрудников Вашей Компании за отченый период:\n')
    staff = int(staff)
    print('Прибыль на одного сотрудника в отчетном периоде составила:', comp_1 / staff, 'тыс.р. на человека')
else:
    print('Ваша Компания имеет годовой убыток:',comp_1)

'''6. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров. 
Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего. 
Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров. 
Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
Например: a = 2, b = 3.
Результат:
1-й день: 2
2-й день: 2,2
3-й день: 2,42
4-й день: 2,66
5-й день: 2,93
6-й день: 3,22
Ответ: на 6-й день спортсмен достиг результата — не менее 3 км.'''
print("-" * 50)
print('task_6')
a = input('Введите результат спортсмена в первый день(км.):\n')
b = input('Введите требуемый  для спортсмена минимум (км.):\n')
a = int(a)
b = int(b)
i = 1
while a < b:
    a *= 1.1
    i += 1
print('на ',i,'день спортсмен достиг результата — не менее',b, 'км.')