# Задача
# Написать игру в “Крестики-нолики”. Можете использовать
# любые парадигмы, которые посчитаете наиболее
# подходящими. Можете реализовать доску как угодно - как
# одномерный массив или двумерный массив (массив массивов).
# Можете использовать как правила, так и хардкод, на своё
# усмотрение. Главное, чтобы в игру можно было поиграть через
# терминал с вашего компьютера.


# использую парадигму ООП
# создаю класс с игрой
class TicTacToe:
    # инициализация класса проходит без передачи дополнительных параметров
    def __init__(self):
        self.field = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.player_move = 'X'

    # наполняю класс защищенными методами для внутреннего использования по отрисовки поля, передаче хода и  проверке на выигрышные позции
    def __draw_field(self):
        print('-------------')
        for i in range(3):
            print('|', self.field[0 + i * 3], '|', self.field[1 + i * 3], '|', self.field[2 + i * 3], '|')
            print('-------------')

    def __move_in_game(self, player: str):
        self.player_move = player
        value = False
        while not value:
            player_choice = input(f'Ход делает {self.player_move}: ')
            try:
                player_choice = int(player_choice)
            except:
                print('Вы ввели некорректное значение. Попробуйте еще раз.')
                continue
            if 9 >= player_choice >= 1:
                if str(self.field[player_choice - 1]) not in 'XO':
                    self.field[player_choice - 1] = self.player_move
                    value = True
                else:
                    print('Невозможно выполнить ход в уже заполненную ячейку. Попробуйте еще раз.')
            else:
                print('Такой ячейки не существует. Попробуйте еще раз.')

    def __winning_positions(self):
        winning_coordinates = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
        for all_ in winning_coordinates:
            if self.field[all_[0]] == self.field[all_[1]] == self.field[all_[2]]:
                return self.field[all_[0]]
        return False

    # прописываю основной метод с игрой, внутри метода используется процедурная парадигма с вызовом методов класса
    def game(self):
        print(chr(128075), ' Давайте начнем игру!')
        count = 0
        while True:
            self.__draw_field()
            if count % 2 == 0:
                self.__move_in_game('X')
            else:
                self.__move_in_game('O')
            count += 1
            if count > 4:
                temp = self.__winning_positions()
                if temp:
                    print(temp)
                    print('Поздравляем! Победа! ', chr(127942))
                    break
            if count == 9:
                print('Ничья!')
                break
        self.__draw_field()


if __name__ == '__main__':
    # Для запуска игры необходимо создать объект класса и вызвать в нем открытый метод game
    game = TicTacToe()
    game.game()
    # при использовании парадигмы ооп мы можем импортировать класс с игрой куда захотим и использовать его там
