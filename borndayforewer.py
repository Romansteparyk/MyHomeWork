""" Опрос.Дата рождения Александра Сергеевича Пушкина """

year0 = 1799
month0 = "Июнь"
day0 = 6

print("Когда  родился Пушкин А.С.?")
year = int(input("Введите год: "))

while year0 != year:
    print ("Ответ не верный!")
    year = int(input("Попробуй ещё раз: "))
print("Правильно!!!")

print("А теперь укажи месяц с большой буквы: ")
month = input("Ваш вариант: ")

while month0 != month:
    print("Ответ не верный!")
    month = input("Попробуй ещё раз: ")
print("Правильно!!")

print("Ты молодец! Осталось указать день месяца.")
day = int(input("Введи свой вариант: "))

while day0 != day:
    print("Неверно. Попробуй ещё разок!")
    day = int(input("Ваш вариант: "))
print("Ты молодец. Александру Сергеевичу было бы приятно!!!")