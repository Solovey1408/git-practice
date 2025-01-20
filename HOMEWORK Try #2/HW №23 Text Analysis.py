# Напишите программу, которая анализирует текст, введенный пользователем, и выполняет следующие действия:
user_in_text = str(input('Введите текст: ')).lower() #Пользователь вводит строку lower переводит строку в нижний регистр

signs = '!,.?@#$%^&*(){}[]:;' # знаки которые нужно удалить из строки

delete_sign = ''.join(i for i in user_in_text if i not in signs) # удаляем знаки из строки, с помощью условия с перебором символов

words = delete_sign.split() #разбиение строки на список слов []

# 1. Подсчитывает количество слов в тексте.
print(f"Количество слов в тексте: {(len(words))}") #считаем слова через len

# 2. Определяет самое длинное слово в тексте.
longest_word = "" #переменная для использования при выводе

for i in words: # перебор списка со словами по каждому слову

    if len(i) > len(longest_word): #условие при котором, сравниваются все слова i в списке между собой

        longest_word = i #если через условие, какое-то слово i больше другого, он становится переменной longest_word

print("Самое длинное слово:", longest_word) #вывод самого длинного слова

# 3. Подсчитывает количество гласных букв (а,е,ё,и,о,у,ы,э,ю,я) в тексте.

vowels = 'аеёиоуыэюя' # все гласные

consonants = 'цкнгшщзхъфвпрлджчсмтьб' #все согласные

delete_consonants = ''.join(i for i in delete_sign if i not in consonants) #заменяем все согласные на пробелы

delete_consonants_without_space = delete_consonants.replace(" ","") #удаляем все пробелы

print("Количество гласных:", len(delete_consonants_without_space)) #выводим количество гласных через len

# 4. Выводит количество раз, которое каждое слово встречается в тексте.

words_and_count = []

for word in words:
    count = 0

    if word in words:
        count += 1

    if word not in words_and_count:
        words_and_count.append(word)

        print(f"Счетчик слов:'{word}':{count}")
