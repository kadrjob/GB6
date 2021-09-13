# Реализовать склонение слова «процент» во фразе «N процентов». Вывести эту фразу на экран отдельной строкой для каждого из чисел в интервале от 1 до 100:

for elem in range(1, 101):
    rest = elem % 10
    if elem in ([11, 12, 13, 14]):
        name = 'процентов'
    elif rest in ([1]):
        name = 'процент'
    elif rest in ([2, 3, 4]):
        name = 'процента'
    else:
        name = 'процентов'

    print('{} {}'.format(elem, name))

# немного другой вариант
print('Вариант 2')
for elem in range(1, 101):
    rest = elem % 10
    if rest in ([1, 2, 3, 4]) and (elem // 10) == 1:
        name = 'процентов'
    elif rest in ([1]):
        name = 'процент'
    elif rest in ([2, 3, 4]):
        name = 'процента'
    else:
        name = 'процентов'

    print('{} {}'.format(elem, name))
