import random

hello_answers = ["hello", "hi", "salam"] # ответы для приветствия
mood_questions = ["how are you?", "what you do?", "necesen?"] #вопросы для ня вар ня йох
mood_answers = ["good, and you?", "not bad", "yaxshi"] # ответы для ня вар ня йох
regular_question = ["how are your grades?", "how old are you?", "veziyyet neterdi?"] # просто так вопросы
user_answer = "" #ответ пользователя
random_index = 0 #рандомный выбор
while(user_answer != "stop"): #чат отвечает пока не напишем stop
    user_answer = input("- ") #вводим ответ пользователя
    if(user_answer in hello_answers): #проверяем если ответ находится в приветствиях
        random_index = random.randint(0,2)
        print(hello_answers[random_index])
    elif(user_answer in mood_questions): #проверяем если находится в ня вар ня йох
        random_index = random.randint(0,2)
        print(mood_answers[random_index])
    else:
        print("i dont understand you")