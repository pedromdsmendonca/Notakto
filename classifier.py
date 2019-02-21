from enum import Enum

# class Fingerprint(Enum):
#     A = 1
#     B = 2
#     C = 3
#     D = 4

class BoardType(Enum):
    b0_empty = 0
    b1_corner = 1
    b1_edge = 2
    b1_center = 3
    b2_adjacent_corner_edge = 4
    b2_adjacent_corner = 5
    b2_corner_center = 6
    b2_opposite_corner_edge = 7
    b2_opposite_corner = 8
    b2_adjacent_edge = 9
    b2_edge_center = 10
    b2_opposite_edge = 11


classifications = {}


class Classifier:
    def __init__(self, board):
        self.board = board

    def corners(self):
        cells = self.board.cells
        c = []
        if cells[0] == 1:
            c.append(1)
        if cells[2] == 1:
            c.append(2)
        if cells[8] == 1:
            c.append(3)
        if cells[6] == 1:
            c.append(4)
        return c

    def edges(self):
        cells = self.board.cells
        e = []
        if cells[1]:
            e.append(1)
        if cells[5]:
            e.append(2)
        if cells[7]:
            e.append(3)
        if cells[3]:
            e.append(4)
        return e

    def empty(self):
        return self.count() == 0

    def count(self):
        return sum(self.board.cells)

    def has_center(self):
        return self.board.cells[4] == 1

    def has_corner(self):
        cells = self.board.cells
        return cells[0] == 1 or cells[2] == 1 or cells[6] == 1 or cells[8] == 1

    def has_edge(self):
        cells = self.board.cells
        return cells[1] == 1 or cells[3] == 1 or cells[5] == 1 or cells[7] == 1

    def num_adjacent_edges(self):
        count = 0
        edges = self.edges()
        if set([1, 2]) & set(edges) == set([1, 2]):
            count = count + 1
        if set([2, 3]) & set(edges) == set([2, 3]):
            count = count + 1
        if set([3, 4]) & set(edges) == set([3, 4]):
            count = count + 1
        if set([1, 4]) & set(edges) == set([1, 4]):
            count = count + 1
        return count

    def num_adjacent_corners(self):
        count = 0
        corners = self.corners()
        if set([1, 2]) & set(corners) == set([1, 2]):
            count = count + 1
        if set([2, 3]) & set(corners) == set([2, 3]):
            count = count + 1
        if set([3, 4]) & set(corners) == set([3, 4]):
            count = count + 1
        if set([1, 4]) & set(corners) == set([1, 4]):
            count = count + 1
        return count

    def num_adjacent_corners_edges(self):
        count = 0
        corners = self.corners()
        edges = self.edges()
        if 1 in corners and 1 in edges:
            count = count + 1
        if 1 in corners and 4 in edges:
            count = count + 1
        if 2 in corners and 1 in edges:
            count = count + 1
        if 2 in corners and 2 in edges:
            count = count + 1
        if 3 in corners and 2 in edges:
            count = count + 1
        if 3 in corners and 3 in edges:
            count = count + 1
        if 4 in corners and 3 in edges:
            count = count + 1
        if 4 in corners and 4 in edges:
            count = count + 1
        return count

    def classify(self):
        n = self.count()

        # 0
        if n == 0:
            return BoardType.b0_empty
        # 1
        if n == 1:
            if self.has_center():
                return BoardType.b1_center
            if self.has_corner():
                return BoardType.b1_corner
            if self.has_edge():
                return BoardType.b1_edge

        # 2
        if n == 2:
            if self.has_center():
                if self.has_edge():
                    return BoardType.b2_edge_center
                if self.has_corner():
                    return BoardType.b2_corner_center
            if self.has_corner():
                if self.has_edge():
                    if self.num_adjacent_corners_edges() == 1:
                        return BoardType.b2_adjacent_corner_edge
                    else:
                        return BoardType.b2_opposite_corner_edge
                if self.num_adjacent_corners() == 1:
                    return BoardType.b2_adjacent_corner
                else:
                    return BoardType.b2_opposite_corner
            else:
                if self.num_adjacent_edges() == 1:
                    return BoardType.b2_adjacent_edge
                else:
                    return BoardType.b2_opposite_edge

        # 3


