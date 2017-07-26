# -*- coding: utf-8 -*-

u"""игра Крестики-Нолики"""

__author__ = "Sybkoi"


class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def game_start(self):
        while True:
            if not self.player1.is_free_cell():
                print("draw")
                break
            self.player1.step()
            if self.player1.is_winner():
                print("player1 is winner!")
                break
            if not self.player2.is_free_cell():
                print("draw")
                break
            self.player2.step()
            if self.player2.is_winner():
                print("player2 is winner")
                break


class Player:
    def __init__(self, field, marker):
        self.field = field
        self.marker = marker

    def is_free_cell(self):
        return self.field.is_free_cell()

    def step(self):
        pass

    def is_winner(self):
        return self.field.is_line(self.marker)


class Human(Player):
    def __init__(self, field, marker):
        Player.__init__(self, field, marker)

    def step(self):
        while True:
            x = int(input("Enter x:"))
            y = int(input("Enter y:"))
            if self.field.is_empty_cell(x, y):
                self.field.mark(x, y, self.marker)
                self.field.show()
                break
            else:
                print("Cell is full! Try another one.")


class Computer(Player):
    def __init__(self, field, marker):
        Player.__init__(self, field, marker)

    def step(self):
        (x, y) = self.field.get_free_cell()
        self.field.mark(x, y, self.marker)
        self.field.show()


class Field:
    def __init__(self):
        self.cells = []
        for i in range(0, 3):
            temp = []
            for j in range(0, 3):
                temp.append(Cell())
            self.cells.append(temp)

    def is_free_cell(self):
        for i in range(0, 3):
            for j in range(0, 3):
                if self.cells[i][j].status == "P":
                    return True
        return False

    def is_line(self, mark):
        for i in range(0, 3):
            if (self.cells[i][0].status == mark and
                self.cells[i][1].status == mark and
                self.cells[i][2].status == mark):
                return True

        for i in range(0, 3):
            if (self.cells[0][i].status == mark and
                self.cells[1][i].status == mark and
                self.cells[2][i].status == mark):
                return True

        if (self.cells[0][0].status == mark and
            self.cells[1][1].status == mark and
            self.cells[2][2].status == mark):
            return True

        if (self.cells[0][2].status == mark and
            self.cells[1][1].status == mark and
            self.cells[2][0].status == mark):
            return True

        return False

    def mark(self, x, y, mark_type):
        self.cells[x][y].status = mark_type

    def show(self):
        for i in range(0, 3):
            print("{} {} {}".format(self.cells[i][0].status, self.cells[i][1].status, self.cells[i][2].status))
        print("-"*7)

    def get_free_cell(self):
        for i in range(0, 3):
            for j in range(0, 3):
                if self.cells[i][j].status == "P":
                    return (i, j)

    def is_empty_cell(self, x, y):
        if self.cells[x][y].status == "P":
            return True


class Cell:
    def __init__(self):
        self.status = "P"


def main():
    field = Field()
    player1 = Human(field, "X")
    player2 = Computer(field, "O")
    g = Game(player1, player2)
    g.game_start()

if __name__ == "__main__":
    main()






