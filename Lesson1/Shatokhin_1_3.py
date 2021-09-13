# Реализовать склонение слова «процент» во фразе «N процентов». Вывести эту фразу на экран отдельной строкой для каждого из чисел в интервале от 1 до 100:

for elem in range(1,101):
    rest = elem % 10
    if (elem) in ([11, 12, 13, 14]):
        str = 'процентов'
    elif (rest) in ([1]):
        str = 'процент'
    elif (rest) in ([2,3,4]):
        str = 'процента'
    else: str ='процентов'

    print('{} {}'.format(elem,str))

# немного другой вариант
print('Вариант 2')
for elem in range(1, 101):
    rest = elem % 10
    if (rest) in ([1, 2, 3, 4]) and (elem // 10) == 1:
        str = 'процентов'
    elif (rest) in ([1]):
        str = 'процент'
    elif (rest) in ([2, 3, 4]):
        str = 'процента'
    else:
        str = 'процентов'

    print('{} {}'.format(elem, str))