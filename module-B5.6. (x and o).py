# Функции
# Приветствие и правила игры

def hello():
    print("*******************************************************")
    print("*                    Здравствуй!                      *")
    print("*         Я хочу сыграть с тобой в одну игру!         *")
    print("*                  КРЕСТИКИ И НОЛИКИ                  *")
    print("*******************************************************")
    print("*               Для игры Вам понадобится              *")
    print("*        вводить следующие данные через пробел        *")
    print("*                   Номер строки: Х                   *")
    print("*                   Номер столбца: Y                  *")
    print("*******************************************************")

#Отображение игрового поля с ячейками

def show():
    print("       0   1   2       ")
    print("     ..............    ")
    for i, row in enumerate(cell):
        row_str = f"   {i} : {' : '.join(row)} : "
        print(row_str)
        print("     ..............    ")
    print()

# Ввод X и Y

def ask():
    while True:
        cords = input("        Ваш ход: ").split()
        if len(cords) != 2:
            print(" Введите координаты: X и Y ! ")
            continue

        x, y = cords

        if not (x.isdigit) or not (y.isdigit()):
            print(" Введите X и Y ")
            continue
        x, y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 2 :
            print(" ВЫ ввели значения вне диапозона! ")
            continue
        if cell [x][y] != " ":
            print(" Данная клетка занята, попробуйте еще раз! ")
            continue
        return x, y

# Проверка комбинаций WIN

def chek_win():
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(cell[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
                print("!!! X - WIN !!!")
                return True

        if symbols == ["O", "O", "O"]:
                print("!!! O - WIN !!!")
                return True
    return False

# Запуск игры

hello()
cell = [[" "] * 3 for i in range(3)]
count = 0
while True:
    count += 1
    show()
    if count % 2 == 1:
        print(" Ходит игрок - Х ")
    else:
        print(" Ходит игрок - O ")

    x, y = ask()

    if chek_win():
        break

    if count % 2 == 1:
        cell[x][y] = "X"
    else:
        cell[x][y] = "O"

    if chek_win():
        break

    if count == 9:
        print(" !!! Игра окончена - НИЧЬЯ !!!")
        break