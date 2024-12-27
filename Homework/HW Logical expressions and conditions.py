question_1 = str(input('Вам есть 18 лет: '))
question_2 = str(input('Вы гражданин страны: '))
question_3 = str(input('Вы были дисквалифицированы: '))

if question_1 == 'Да' and question_2 == 'Да' and question_3 == 'Нет':
    print('Вы допущены к выборам')
else:
    print('Вы не допущены к выборам')