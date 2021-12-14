from graphics import *
from classifier import *
from enum import Enum

class Board:
    def __init__(self):
        self.cells = [0 for i in range(9)]
        self.over = False

    def print_board(self):
        print ("{}|{}|{}".format(self.print_cell(0),self.print_cell(1),self.print_cell(2)))
        print ("-----")
        print ("{}|{}|{}".format(self.print_cell(3),self.print_cell(4),self.print_cell(5)))
        print ("-----")
        print ("{}|{}|{}".format(self.print_cell(6),self.print_cell(7),self.print_cell(8)))

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
        if (self.check_row_complete(0, 1, 2) or self.check_row_complete(3, 4, 5) or
                self.check_row_complete(6, 7, 8) or self.check_row_complete(0, 3, 6) or
                self.check_row_complete(1, 4, 7) or self.check_row_complete(2, 5, 8) or
                self.check_row_complete(0, 4, 8) or self.check_row_complete(2, 4, 6)):
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
            print ("---------------")

    def play(self, board, pos):
        if self.boards[board].try_play(pos):
            if self.game_over():
                self.over = True
                self.winning_player = 1 - self.active_player
            self.active_player = 1 - self.active_player
            return True
        return False

    def game_over(self):
        return self.boards[0].over and self.boards[1].over and self.boards[2].over

    def board_is_over(self, board):
        return self.boards[board].over


def create_game_board():
    label = Text(Point(650, 50), 'Notakto')
    label.setTextColor('grey')
    label.setStyle('italic')
    label.setSize(20)
    label.draw(win)

    create_single_board(100,100,400,400)
    create_single_board(500,100,800,400)
    create_single_board(900,100,1200,400)

    display_block_board()

    set_active_player_text()


def create_single_board(xmin, ymin, xmax, ymax):
    board_outline = Rectangle(Point(xmin, ymin), Point(xmax, ymax))  # Draw rectangle
    board_outline.setFill('grey')
    board_outline.setOutline('cyan')
    board_outline.setWidth(3)
    board_outline.draw(win)

    draw_vertical_separator(xmin+100, ymin, ymax)
    draw_vertical_separator(xmin+200, ymin, ymax)
    draw_horizontal_separator(xmin, xmax, ymin+100)
    draw_horizontal_separator(xmin, xmax, ymin+200)


def draw_vertical_separator(x, ymin, ymax):
    separator = Line(Point(x, ymin), Point(x, ymax))  # set endpoints
    separator.setOutline('cyan')
    separator.setWidth(3)
    separator.draw(win)


def draw_horizontal_separator(xmin, xmax, y):
    separator = Line(Point(xmin, y), Point(xmax, y))  # set endpoints
    separator.setOutline('cyan')
    separator.setWidth(3)
    separator.draw(win)


def set_active_player_text():
    player = 1 if game.active_player == 1 else 2
    text.setTextColor('red' if player == 1 else 'blue')
    text.setStyle('bold')
    text.setSize(32)
    text.setText('Player ' + str(player))


def disable_board(board):
    overlay = Rectangle(Point(100 + board*400, 100), Point(400 + board*400, 400))
    overlay.setFill('red')
    overlay.draw(win)


def mouse_events_handling():
    while True:
        p1 = win.getMouse()
        x = p1.getX()
        y = p1.getY()
        if 400 > x > 100 and 400 > y > 100:  # filter board
            board = 0
        elif 800 > x > 500 and 400 > y > 100:  # filter board
            board = 1
            x = x-400
        elif 1200 > x > 900 and 400 > y > 100:  # filter board
            board = 2
            x = x-800
        else:
            continue
        x = int((x-100)//100)
        y = int((y-100)//100)
        pos = y*3 + x
        if game.play(board, pos):
            bt1 = Classifier(game.boards[0]).classify()
            bt2 = Classifier(game.boards[1]).classify()
            bt3 = Classifier(game.boards[2]).classify()
            c1 = classifications[bt1]
            c2 = classifications[bt2]
            c3 = classifications[bt3]

            fp1.setText(FingerprintEnum(c1).name)
            fp2.setText(FingerprintEnum(c2).name)
            fp3.setText(FingerprintEnum(c3).name)
            set_active_player_text()
            win.items[board*9+pos].setText('X')
            win.items[board * 9 + pos].setTextColor('red' if game.active_player == 0 else 'blue')
            if game.board_is_over(board):
                disable_board(board)
            game.print_game()
            if game.over:
                game_over()


def display_block_board():
    for i in range(27):
        win.items[i].setTextColor('cyan')
        win.items[i].setStyle('bold')
        win.items[i].setSize(32)
        win.items[i].draw(win)


def set_block_list():
    for i in range(9):
        tile = Text(Point(150+(i%3)*100, 150+(i//3)*100), ' ')
        win.items.append(tile)
    for i in range(9):
        tile = Text(Point(400+150+(i%3)*100, 150+(i//3)*100), ' ')
        win.items.append(tile)
    for i in range(9):
        tile = Text(Point(800+150+(i%3)*100, 150+(i//3)*100), ' ')
        win.items.append(tile)


def game_over():
    message = Text(Point(250, 422), "Congratulations Player {} You won the game".format(game.winning_player))
    message.setTextColor('black')
    message.setStyle('italic')
    message.setSize(10)
    message.draw(win)


game = Game()

win = GraphWin('Notakto', 1300, 500, autoflush=False)  # give title and dimensions
win.items = []

# set_active_player_text()
set_block_list()

text = Text(Point(650, 450), 'what')
text.setSize(10)
text.setStyle('bold')
text.setTextColor('green')
text.draw(win)

fp1 = Text(Point(250, 75), 'fp1')
fp1.setSize(16)
fp1.setStyle('bold')
fp1.setTextColor('red')
fp1.draw(win)
fp2 = Text(Point(650, 75), 'fp2')
fp2.setSize(16)
fp2.setStyle('bold')
fp2.setTextColor('red')
fp2.draw(win)
fp3 = Text(Point(1050, 75), 'fp3')
fp3.setSize(16)
fp3.setStyle('bold')
fp3.setTextColor('red')
fp3.draw(win)

create_game_board()
mouse_events_handling()
