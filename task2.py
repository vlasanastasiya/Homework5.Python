# Создайте программу для игры в ""Крестики-нолики"".

print("Игра крестики нолики")
field = list(range(1,10))

def input_field(field):   #создаем поле для игры
    print ("-------------")
    for i in range(3):
        print ("|",field[0+i*3], "|",field[1+i*3], "|",field[2+i*3], "|")
        print ("-------------")
                        
def players_move(players):  #проверяем ход игрока
   valid = False
   while not valid:
      step = input("В какую ячейку разместим " + players+"? ")
      try:
         step = int(step)
      except:
         print("Неправильный ввод")
         continue
      if step >= 1 and step <= 9:
         if(str(field[step-1]) not in "XO"):
            field[step-1] = players
            valid = True
         else:
            print("Ячейка используется")
      else:
        print("Неправильный ввод")   

def winner(field):  #проверяем победителя
        lines = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
        for i in lines:
                if field[i[0]] == "X" and field[i[1]] == "X" and field[i[2]] == "X":
                        win = "X"
                if field[i[0]] == "O" and field[i[1]] == "O" and field[i[2]] == "O":
                        win = "O"
        return win

def game(field):
        count = 0
        winner_player = False
        while not winner_player:
                input_field(field)
                if count % 2 == 0:
                        players_move("X")
                else:
                        players_move("O")
                count +=1
                if count > 4:
                        temp = winner(field)      
                        if temp:
                                print("\n" + temp, "победа")
                                winner_player = True
                                break
                        if count == 9:
                                print(" у нас ничья")
                                break
        input_field(field)

game(field)



         