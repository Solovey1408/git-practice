question_1 = str(input('Вам есть 18 лет: ')).lower()
question_2 = str(input('Вы гражданин страны: ')).lower()
question_3 = str(input('Вы были дисквалифицированы: ')).lower()

if question_1 == 'да' and question_2 == 'да' and question_3 == 'нет':
    print('Вы допущены к выборам')
else:
    print('Вы не допущены к выборам')