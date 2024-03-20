# Крестики-ноликик на языке программирования python
# -------------------------------------------------

# Количество клеток
board_size = 3
#Номерация игрового поля
board = []
for element in range(1,10):
    board.append(element)

# Вывод игрового поля
def draw_board():
    print("_" * 4 * board_size)
    for i in range(board_size):
        print((" " * 3 + "|")*board_size)
        print(board[i * board_size], " |", board[1 + i * board_size], "|", board[2 + i * board_size], "|")
        print(("_" * 3 + '|')*board_size)

# Выполняем ход
def game_step(index, char):
    if (index > 9 or index < 1 or board[index - 1] in ("X", " O")):
        return False
    board[index - 1] = char
    return True

# Проверка на победу одного из игроков
def check_win():
    win = False

    win_combination = (
        (0,1,2), (3,4,5), (6,7,8), # горизонтальные линии
        (0,3,6), (1,4,7), (2,5,8), # вертикальные линии
        (0,4,8), (2,4,6)           # диагональные
    )

    for pos in win_combination:
        if(board[pos[0]] == board[pos[1]] and board[pos[1]] == board[pos[2]]):
            win = board[pos[0]]
    return win

def start_game():
    #текущий игрок
    current_player = "X"
    #номер шага
    step = 1
    draw_board()

    while (step <= 9) and (check_win() == False):
        index = input("Ходит игрок " + current_player + ". Веедите номер поля (0 - выход):")

        #Проверка на правильный ввод пользователя (0-9)
        proverka = False
        for i in range(10):
            if index == str(i):
                proverka = True

        if proverka:
            if (index == "0"):
                break

            # Если получилось сделать шаг
            if(game_step(int(index), current_player)):
                print("Ход игрока сделан")

                if(current_player == "X"):
                    current_player = "O"
                else:
                    current_player = "X"

                draw_board()

                #Увеличим номер хода
                step += 1

            else:
                print("Неверный номер. Повторите свой ход")
        else:
            print("Вы ввели не номер клетки, пожалуйста, повторите свой ход")

    if(step == 10):
        print("Игра окончена. Ничья!")
    else:
        print("Выйграл" + check_win())

print("Добро пожаловать в крестики-нолики на python")
start_game()