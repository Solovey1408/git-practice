text = str(input("Введите текст: ")).lower() #lower перевод строки в ниж.регистр

#ПОДСЧЕТ КОЛИЧЕСТВА СЛОВ В ТЕКСТЕ
sign = '()-[]{};\\\',<>./!?@#$%^&*_~:+' #Символы, которые не нужно учитывать
text_without_sign = "".join(char for char in text if char not in sign) #Объединяет список строк в одну строку,
#используя "" в качестве разделителя (условие for чтобы убрать знаки из переменной yes_sign)

split_text = text_without_sign.split() #split - Разбивает предложение на список слов ['слово', 'слово', 'слово']

count = 0 #счетчик слов, который изначально 0
for char in split_text: #char - это один элемент в списке
    count += 1 #счетчик слов, который прибавляет один после каждого слова

print("Кол-во слов в тексте:", count) #Вывод переменной, к которой прибавили все слова в списке

#ПОИСК САМОГО ДЛИННОГО СЛОВА В ТЕКСТЕ
words = dict()
for word in text.split(" "):
    words[len(word)] = word

long_word = words[max(words)]
print("Самое длинное слово:", long_word)

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

#vowels_count =  sum(letter in vowels for letter in text)
#print(s.vowels_count("aeёиоуыэюя"))
#print("Количество дублирования слов:", counting_words)
#Что ? Где ! Когда .