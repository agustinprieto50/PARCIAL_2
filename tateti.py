class TaTeTi():
    def __init__(self, piece=""):
        self.board = {'1.1': '1.1', '1.2': '1.2', '1.3': '1.3',
                      '2.1': '2.1', '2.2': '2.2', '2.3': '2.3',
                      '3.1': '3.1', '3.2': '3.2', '3.3': '3.3'}
        self.valid = ['1.1', '1.2', '1.3',
                      '2.1', '2.2', '2.3',
                      '3.1', '3.2', '3.3']
        self.piece = piece

    def __str__(self):
        board = '1.1|1.2|1.3\n---+---+---\n2.1|2.2|2.3\n'
        board += '---+---+---\n3.1|3.2|3.3'
        return board

    def input_position(self):
        valido = True
        while valido is True:
            pos = (input("posicion: "))
            if pos in self.valid:
                key = self.valid.index(pos)
                self.valid.pop(key)
                return pos
                valido = False

    def win(self):
        if self.board["1.1"] == self.board["1.2"] and self.board["1.1"] == self.board["1.3"]:
            return True
        if self.board["1.1"] == self.board["2.1"] and self.board["1.1"] == self.board["3.1"]:
            return True
        if self.board["1.1"] == self.board["2.2"] and self.board["1.1"] == self.board["3.3"]:
            return True
        if self.board["1.2"] == self.board["2.2"] and self.board["1.2"] == self.board["3.2"]:
            return True
        if self.board["1.3"] == self.board["2.3"] and self.board["1.3"] == self.board["3.3"]:
            return True
        if self.board["1.3"] == self.board["2.2"] and self.board["1.3"] == self.board["3.1"]:
            return True
        if self.board["2.1"] == self.board["2.2"] and self.board["2.1"] == self.board["2.3"]:
            return True
        if self.board["3.1"] == self.board["3.2"] and self.board["3.1"] == self.board["3.3"]:
            return True
        return False

    def game(self):
        print(self)
        while not self.win() and len(self.valid) > 0:
            self.board[self.input_position()] = ' ' + self.piece + ' '
            print(self)
            winner = self.piece
            self.piece = 'o' if self.piece == 'x' else 'x'
        if len(self.valid) == 0:
            winner = 'Ninguno'
        return winner


if __name__ == '__main__':
    game = TaTeTi()

    print('Ganó ' + game.game())
