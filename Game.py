import os
from graphics import *

class Board:
    def __init__(self):
        self.cells = [0 for i in range(9)]
        self.over = False

    def print_board(self):
        print "{}|{}|{}".format(self.print_cell(0),self.print_cell(1),self.print_cell(2))
        print "-----"
        print "{}|{}|{}".format(self.print_cell(3),self.print_cell(4),self.print_cell(5))
        print "-----"
        print "{}|{}|{}".format(self.print_cell(6),self.print_cell(7),self.print_cell(8))

    def print_cell(self, index):
        return "X" if self.cells[index] == 1 else " "

    def try_play(self, index):
        if self.over:
            return False
        if self.cells[index] == 1:
            return False
        else:
            self.cells[index] = 1
            self.check_board_over()
            return True

    def check_board_over(self):
        if (self.check_row_complete(0, 1, 2) or
            self.check_row_complete(3,4,5) or
            self.check_row_complete(6,7,8) or
            self.check_row_complete(0,3,6) or
            self.check_row_complete(1,4,7) or
            self.check_row_complete(2,5,8) or
            self.check_row_complete(0,4,8) or
            self.check_row_complete(2,4,6)):
            self.over = True
        return self.over

    def check_row_complete(self, r1, r2, r3):
        return self.cells[r1] == self.cells[r2] == self.cells[r3] == 1

class Game:
    def __init__(self):
        self.boards = [Board() for i in range(3)]
        self.active_player = 1
        self.over = False
        self.winning_player = -1

    def print_game(self):
        for b in self.boards:
            b.print_board()
            print "---------------"

    def play(self, board, pos):
        if self.boards[board].try_play(pos):
            if self.game_over():
                self.over = True
                self.winning_player = self.active_player
            self.active_player = 1 - self.active_player
            return True
        return False

    def game_over(self):
        return self.boards[0].over and self.boards[1].over and self.boards[2].over

def create_game_board():
    label = Text(Point(250, 50), 'Tic-Tac-Toe')
    label.setTextColor('grey')
    label.setStyle('italic')
    label.setSize(20)
    label.draw(win)

    board_outline_2 = Rectangle(Point(500, 100), Point(800, 400))  # Draw rectangle
    board_outline_2.setFill('grey')
    board_outline_2.setOutline('cyan')
    board_outline_2.setWidth(3)
    board_outline_2.draw(win)

    board_outline_3 = Rectangle(Point(900, 100), Point(1200, 400))  # Draw rectangle
    board_outline_3.setFill('grey')
    board_outline_3.setOutline('cyan')
    board_outline_3.setWidth(3)
    board_outline_3.draw(win)



def create_single_board(xmin, ymin, xmax, ymax):
    board_outline_1 = Rectangle(Point(xmin, ymin), Point(xmax, ymax))  # Draw rectangle
    board_outline_1.setFill('grey')
    board_outline_1.setOutline('cyan')
    board_outline_1.setWidth(3)
    board_outline_1.draw(win)

    # boards_separator_1 = Line(Point(200, 100), Point(200, 400))  # set endpoints
    # boards_separator_1.setOutline('cyan')
    # boards_separator_1.setWidth(3)
    # boards_separator_1.draw(win)

win = GraphWin('Tic-Tac-Toe', 1300, 500, autoflush=False) # give title and dimensions

create_game_board()

game = Game()

#game loop
os.system('clear')
while not game.over:
    game.print_game()
    # TODO sanitize input
    move = raw_input("Player 1\n" if game.active_player == 1 else "Player 2\n")
    split = move.split(' ')
    # if len(split) != 2:
    #     print "invalid input!"
    #     continue;
    b, p = split
    b, p = int(b), int(p)
    while not game.play(b, p):
        move = raw_input("Player 1\n" if game.active_player == 1 else "Player 2\n")
        split = move.split(' ')
        b, p = split
        b, p = int(b), int(p)
    os.system('clear')

game.print_game()
print "Player 1" if game.winning_player == 1 else "Player 2"
print "WON!"