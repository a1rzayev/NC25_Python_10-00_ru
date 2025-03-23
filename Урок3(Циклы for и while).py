"""цикл for"""
lap_count = 10 #количество кругов
for i in range(1, lap_count+1): #(start,end(не включительно),step)
    print("Круг", i, "/", lap_count)
print("Финиш")

"""цикл while"""
Artem_position = 0 #позития Артёма
Nail_position = 10 #позития Наиля
while(Artem_position < Nail_position): #пока Артём не дошёл до Наиля
    Artem_position = Artem_position + 1 #позиция Артёма увеличивается на 1(он ходит)
    print("Артём находится на:", Artem_position)
    print("Наиль находится на:", Nail_position)
    print()