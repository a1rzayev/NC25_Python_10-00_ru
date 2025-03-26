import random

print("добро пожаловать в игру *камень, ножницы, бумага*") #приветствие
move_list = ["камень", "ножницы", "бумага"] #list список ходов
player_answer = "" #str ответ игрока
bot_answer = "" #str ответ бота
bot_score = 0 #int счёт бота
player_score = 0 #int счёт игрока
random_index = 0 #int рандомный индекс, для ответа бота
while(player_answer != "stop"): #игра продолжается пока не напишем stop
    player_answer = input("камень, ножницы или бумага: ") #вводим выбор пользователя
    if(player_answer == "stop"):
        break
    if(player_answer != "камень" and player_answer != "ножницы" and player_answer != "бумага"): #если неправильный ввод
        print("введи правильный ход!")
        print()
        continue
    random_index = random.randint(0, 2) #рандомный выбор бота
    bot_answer = move_list[random_index] #готовим ответ бота
    print("бот: ", bot_answer)
    if(player_answer == bot_answer): #если ответы одинаковые
        print("ничья!") #то ничья
        #выводим счёт
        print("игрок: ", player_score)
        print("бот: ", bot_score)
        print()

    elif(player_answer == "камень" and bot_answer == "ножницы"):
        print("вы выиграли!") #то выиграл игрок
        player_score = player_score + 1 #добавляем к счёту игрока 1 балл
        #выводим счёт
        print("игрок: ", player_score)
        print("бот: ", bot_score)
        print()    
    elif(player_answer == "камень" and bot_answer == "бумага"):
        print("бот выиграл!") #то выиграл бот
        bot_score = bot_score + 1 #добавляем к счёту бота 1 балл
        #выводим счёт
        print("игрок: ", player_score)
        print("бот: ", bot_score)
        print()    

    elif(player_answer == "бумага" and bot_answer == "камень"):
        print("вы выиграли!") #то выиграл игрок
        player_score = player_score + 1 #добавляем к счёту игрока 1 балл
        #выводим счёт
        print("игрок: ", player_score)
        print("бот: ", bot_score)
        print()    
    elif(player_answer == "бумага" and bot_answer == "ножницы"):
        print("бот выиграл!") #то выиграл бот
        bot_score = bot_score + 1 #добавляем к счёту бота 1 балл
        #выводим счёт
        print("игрок: ", player_score)
        print("бот: ", bot_score)
        print()    

    elif(player_answer == "ножницы" and bot_answer == "бумага"):
        print("вы выиграли!") #то выиграл игрок
        player_score = player_score + 1 #добавляем к счёту игрока 1 балл
        #выводим счёт
        print("игрок: ", player_score)
        print("бот: ", bot_score)
        print()    
    elif(player_answer == "ножницы" and bot_answer == "камень"):
        print("бот выиграл!") #то выиграл бот
        bot_score = bot_score + 1 #добавляем к счёту бота 1 балл
        #выводим счёт
        print("игрок: ", player_score)
        print("бот: ", bot_score)
        print()    
    
print() 
print("игрок: ", player_score)
print("бот: ", bot_score)
print("до свидания!") #прощание