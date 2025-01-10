text = str(input("Введите текст: ")).lower() #lower перевод строки в ниж.регистр

#ПОДСЧЕТ КОЛИЧЕСТВА СЛОВ В ТЕКСТЕ
sign = '()-[]{};\\\',<>./!?@#$%^&*_~:+' #Символы, которые не нужно учитывать
text_without_sign = "".join(char for char in text if char not in sign) #Объединяет список строк в одну строку,
#используя "" в качестве разделителя (условие for чтобы убрать знаки из переменной sign)

split_text = text_without_sign.split() #split - Разбивает предложение на список слов ['слово', 'слово', 'слово']
words_counter = len(split_text)

print("Кол-во слов в тексте:", words_counter) #Вывод переменной, к которой прибавили все слова в списке

#ПОИСК САМОГО ДЛИННОГО СЛОВА В ТЕКСТЕ
longest_word = ""

for word in split_text:
    if len(word) > len(longest_word):
        longest_word = word
print("Самое длинное слово:", longest_word)

#ПОДСЧЕТ ГЛАСНЫХ БУКВ В ТЕКСТЕ
count_vowels = 0 #счетчик для подсчета гласных, изначально 0
vowels = 'аеёиоуыэюя' #Переменная с гласными

for i in text_without_sign: #Перебор элемента в тексте
    if i in vowels: #Перебор элементов в переменной гласные
        count_vowels += 1 #Счетчик гласных
print("Кол-во гласных в тексте:", count_vowels)

#ПОДСЧЕТ СЛОВ В ТЕКСТЕ
word_count = {}

for word in split_text:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

for word, count in word_count.items():
    print(f"Счетчик слов:'{word}':{count}")

#Что ? Где ! Когда .