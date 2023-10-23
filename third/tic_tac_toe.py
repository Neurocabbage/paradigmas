# ● Контекст
# Вероятнее всего, вы с детства знакомы с этой игрой. Пришло
# время реализовать её. Два игрока по очереди ставят крестики
# и нолики на игровое поле. Игра завершается когда кто-то
# победил, либо наступила ничья, либо игроки отказались
# играть.
# ● Задача
# Написать игру в “Крестики-нолики”. Можете использовать
# любые парадигмы, которые посчитаете наиболее
# подходящими. Можете реализовать доску как угодно - как
# одномерный массив или двумерный массив (массив массивов).
# Можете использовать как правила, так и хардкод, на своё
# усмотрение. Главное, чтобы в игру можно было поиграть через
# терминал с вашего компьютера.

class Board:
    def __init__(self):
        self.board = [[None, None, None], [None, None, None], [None, None, None]]

    def draw(self):
        for row in self.board:
            print(row)

    def check_win(self, player):
        # Проверка строк и столбцов
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] == player or \
               self.board[0][i] == self.board[1][i] == self.board[2][i] == player:
                return True

        # Проверка диагоналей
        if self.board[0][0] == self.board[1][1] == self.board[2][2] == player or \
           self.board[0][2] == self.board[1][1] == self.board[2][0] == player:
            return True

        return False

    def make_move(self, row, col, player_token):
        if self.board[row][col] is None:
            self.board[row][col] = player_token
            return True
        else:
            return False

    def is_full(self):
        for row in self.board:
            if None in row:
                return False
        return True


class Player:
    def __init__(self, token):
        self.token = token

    def make_move(self, board):
        while True:
            try:
                row, col = map(int, input(f"Куда поставим {self.token}? Введите координаты через пробел: ").split())
                if 0 <= row <= 2 and 0 <= col <= 2:
                    if board.make_move(row, col, self.token):
                        break
                    else:
                        print("Эта клетка уже занята!")
                else:
                    print("Некорректный ввод. Введите два числа от 0 до 2.")
            except ValueError:
                print("Некорректный ввод. Введите два числа от 0 до 2.")


def play_game():
    board = Board()
    players = [Player("X"), Player("O")]
    current_player = players[0]

    while True:
        board.draw()
        current_player.make_move(board)

        if board.check_win(current_player.token):
            board.draw()
            print(f"Игрок {current_player.token} победил!")
            break
        elif board.is_full():
            board.draw()
            print("Ничья!")
            break

        players.reverse()
        current_player = players[0]


play_game()

'''
В этой программе использованы ООП (есть классы), процедурная (есть функции) и струтктурная (есть условия и циклы) парадигмы.
'''