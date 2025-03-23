"""Первая версия, когда число каждый раз меняется и мы не знаем больше или меньше угадали"""
import random

print("Угадай число")
print("------------")
random_number = random.randint(1, 100) #число которое выбирает компьютер от 1 до 100
quessed_number = None #абсолютный ноль(т.е. ничего)
try_count = 0 #подсчёт количества попыток
while(random_number != quessed_number): #пока не угадали
    random_number = random.randint(1, 100) #компьютер выбирает компьютер от 1 до 100
    quessed_number = int(input("Введите число: ")) #число которое мы указали
    try_count = try_count + 1 #подсчитываем попытки
    if(random_number != quessed_number): #проверка на угадывание
        print("Неправильный выбор")
print("------------")
print("Вы угадали число!") #когда уже угадали число, цикл while заканчивается и выводится победа
print("Вы загадали за" ,try_count ,"попыток")
    


"""Вторая версия, когда число не меняется каждый раз и мы знаем больше или меньше угадали"""
import random

print("Угадай число")
print("------------")
random_number = random.randint(1, 100) #число которое выбирает компьютер от 1 до 100
quessed_number = None #абсолютное ничего
try_count = 0 #подсчёт количества попыток
while(random_number != quessed_number): #пока не угадали
    quessed_number = int(input("Введите число: ")) #число которое мы указали
    try_count = try_count + 1 #подсчитываем попытки
    if(random_number > quessed_number): #если число которое мы угадали меньше чем загаданное
        print("Меньше чем надо")
    elif(random_number < quessed_number): #если число которое мы угадали больше чем загаданное
        print("Больше чем надо")
print("------------")
print("Вы угадали число!")
print("Вы загадали за" ,try_count ,"попыток")
    