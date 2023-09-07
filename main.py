board = [i for i in range(0, 10)]
vin = ([0, 1, 2],
       [3, 4, 5],
       [6, 7, 8],
       [0, 3, 6],
       [1, 4, 7],
       [2, 5, 8],
       [0, 4, 8],
       [2, 4, 6])


def field_of_play():
    for i in range(3):
        print(board[0 + i * 3], " ", board[1 + i * 3], " ", board[2 + i * 3])


def play_step(index, move):
    if index > 8 or index < 0 or board[index] in ("X", "o"):
        return False
    board[index] = move
    return True


def win_game():
    win = False
    for H in vin:
        if board[H[0]] == board[H[1]] == board[H[2]]:
            win = board[H[1]]
    return win


def game():
    player = "X"
    step_game = 1
    field_of_play()
    while (step_game < 10) and (not win_game()):
        index = int(input(f"Ход игрока, играющего за {player}, введите число с поля: "))
        if play_step(index, player):
            print(f"Ход {player} сделан:")
            field_of_play()
            step_game += 1
            if step_game % 2 == 0:
                player = "о"
            else:
                player = "X"
        else:
            print("Неверно!, введенное Вами число занято или отсутствует на поле, введите другое число: ")
    if not win_game():
        print("Игра окончена!!! Ничья!!! ")
    else:
        print(f"Игра окончена!!! Поздравляем, победил {win_game()}!")


print("Начнем игру крестики-нолики!")
game()
