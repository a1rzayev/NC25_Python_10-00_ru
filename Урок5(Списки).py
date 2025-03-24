class_list = ["Shamil", "Onur", "Nail", "Ayxan",
              "Artem", "Amil", "Mehman", "Amir",
              "Malik", "Medina", "Sara", "Ayhun",
              "Maqa"] #создание списка
              
class_list2 = ["Amil, Mehman, Amir"] #нельзя так создавать!
print(class_list) #вывод списка
print("Index 6:", class_list[6]) #взять элемент из списка

print("Список после добавление Asif")
class_list.append("Asif") #добавление элемента в конец списка
print(class_list)

print("Список после вставки PYTHON")
class_list.insert(1, "PYTHON") #вставка элемента на определённое положение
print(class_list)

print("Список после удаления последнего элемента")
class_list.pop() #удаление последнего элемента
print(class_list)

print("Список после удаления определённого элемента")
class_list.pop(1) #удаление элемента под индексом 1
print(class_list)