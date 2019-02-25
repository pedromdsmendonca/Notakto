from enum import Enum


class FingerprintEnum(Enum):
    I = 0
    A = 1
    B = 2
    C = 3
    D = 4
    C2 = 5
    AD = 6
    AB = 7


class Fingerprint:
    def __init__(self, a=0, b=0, c=0, d=0, fp=-1):
        if fp == -1:
            self.a = a
            self.b = b
            self.c = c
            self.d = d
            return

        self.a = 0
        self.b = 0
        self.c = 0
        self.d = 0

        if fp == FingerprintEnum.I:
            pass
        if fp == FingerprintEnum.A:
            self.a = 1
        if fp == FingerprintEnum.B:
            self.b = 1
        if fp == FingerprintEnum.C:
            self.c = 1
        if fp == FingerprintEnum.D:
            self.d = 1
        if fp == FingerprintEnum.AB:
            self.a = 1
            self.b = 1
        if fp == FingerprintEnum.C2:
            self.c = 2

    def good(self):
        return ((self.a == 1 and self.b == 0 and self.c == 0 and self.d == 0) or
                (self.a == 0 and self.b == 2 and self.c == 0 and self.d == 0) or
                (self.a == 0 and self.b == 1 and self.c == 1 and self.d == 0) or
                (self.a == 0 and self.b == 0 and self.c == 2 and self.d == 0))

    def multiply(self, *others):
        a = self.a
        b = self.b
        c = self.c
        d = self.d

        for other in others:
            a = a + other.a
            b = b + other.b
            c = c + other.c
            d = d + other.d

        return Fingerprint(a, b, c, d)

    def simplify(self):
        pass


class BoardType(Enum):
    b_identity = -1
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
    b3_center_adjacent_corner_edge = 12
    b3_center_opposite_corner_edge = 13
    b3_center_corner = 14
    b3_center_edge = 15
    b3_corner = 16
    b3_only_edges = 17
    b3_only_corners = 18
    b3_adjacent_corners_opposite_edge = 19
    b3_adjacent_edges_opposite_corner = 20
    b3_corner_edge_adjacent_corner = 21
    b3_corner_edge_opposite_corner = 22
    b3_corner_edge_adjacent_edge = 23
    b3_corner_edge_opposite_edge = 24
    b4_center_square = 25
    b4_center_z = 26
    b4_center_t = 27
    b4_center_edges = 28
    b4_center_corners = 29
    b4_edges = 30
    b4_corners = 31
    b4_corners_single_edge = 32
    b4_opposite_adjacent_corner_edges = 33
    b4_adjacent_corner_edge_adjacent_corner_adjacent_edge = 34
    b4_edges_3_no_l = 35
    b4_edges_3_l = 36
    b4_spread_corner = 37
    b4_open_z = 38
    b4_arrow = 39
    b5_center = 40
    b5_edges = 41
    b5_bow = 42
    b5_v = 43
    b5_hook = 44
    b6 = 45


classifications = {
    BoardType.b0_empty: FingerprintEnum.C,
    BoardType.b1_corner: FingerprintEnum.I,
    BoardType.b1_edge: FingerprintEnum.I,
    BoardType.b1_center: FingerprintEnum.C2,
    BoardType.b2_adjacent_corner_edge: FingerprintEnum.AD,
    BoardType.b2_adjacent_corner: FingerprintEnum.B,
    BoardType.b2_corner_center: FingerprintEnum.B,
    BoardType.b2_opposite_corner_edge: FingerprintEnum.B,
    BoardType.b2_opposite_corner: FingerprintEnum.A,
    BoardType.b2_adjacent_edge: FingerprintEnum.A,
    BoardType.b2_edge_center: FingerprintEnum.B,
    BoardType.b2_opposite_edge: FingerprintEnum.A,
    BoardType.b3_corner: FingerprintEnum.B,
    BoardType.b3_center_adjacent_corner_edge: FingerprintEnum.AB,
    BoardType.b3_corner_edge_adjacent_edge: FingerprintEnum.D,
    BoardType.b3_corner_edge_adjacent_corner: FingerprintEnum.A,
    BoardType.b3_corner_edge_opposite_edge: FingerprintEnum.D,
    BoardType.b3_corner_edge_opposite_corner: FingerprintEnum.D,
    BoardType.b3_center_corner: FingerprintEnum.A,
    BoardType.b3_only_corners: FingerprintEnum.AB,
    BoardType.b3_adjacent_corners_opposite_edge: FingerprintEnum.A,
    BoardType.b3_center_opposite_corner_edge: FingerprintEnum.A,
    BoardType.b3_adjacent_edges_opposite_corner: FingerprintEnum.I,
    BoardType.b3_center_edge: FingerprintEnum.AB,
    BoardType.b3_only_edges: FingerprintEnum.B,
    BoardType.b3_only_edges: FingerprintEnum.B,
    BoardType.b4_center_square: FingerprintEnum.A,
    BoardType.b4_edges_3_l: FingerprintEnum.A,
    BoardType.b4_arrow: FingerprintEnum.A,
    BoardType.b4_center_z: FingerprintEnum.B,
    BoardType.b4_center_corners: FingerprintEnum.B,
    BoardType.b4_adjacent_corner_edge_adjacent_corner_adjacent_edge: FingerprintEnum.B,
    BoardType.b4_edges_3_no_l: FingerprintEnum.B,
}


class Classifier:
    def __init__(self, board):
        self.board = board

    def is_over(self):
        return (self.check_row_complete(0, 1, 2) or self.check_row_complete(3, 4, 5) or
                self.check_row_complete(6, 7, 8) or self.check_row_complete(0, 3, 6) or
                self.check_row_complete(1, 4, 7) or self.check_row_complete(2, 5, 8) or
                self.check_row_complete(0, 4, 8) or self.check_row_complete(2, 4, 6))

    def check_row_complete(self, r1, r2, r3):
        return self.board.cells[r1] == self.board.cells[r2] == self.board.cells[r3] == 1

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

    def has_l(self):
        corners = self.corners()
        edges = self.edges()
        if 1 in corners and 1 in edges and 4 in edges:
            return True
        if 2 in corners and 1 in edges and 2 in edges:
            return True
        if 3 in corners and 2 in edges and 3 in edges:
            return True
        if 4 in corners and 3 in edges and 4 in edges:
            return True
        return False

    def classify(self):
        if self.is_over():
            return BoardType.b_identity

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
        if n == 3:
            if self.has_center():
                if self.has_corner():
                    if self.has_edge():
                        if self.num_adjacent_corners_edges() == 1:
                            return BoardType.b3_center_adjacent_corner_edge
                        else:
                            return BoardType.b3_center_opposite_corner_edge
                    else:
                        return BoardType.b3_center_corner
                else:
                    return BoardType.b3_center_edge
            if self.has_corner():
                if self.has_edge():
                    if self.num_adjacent_corners_edges() == 2:
                        return BoardType.b3_corner
                    if self.num_adjacent_corners_edges() == 1:
                        if self.num_adjacent_corners() == 1:
                            return BoardType.b3_corner_edge_adjacent_corner
                        if self.num_adjacent_edges() == 1:
                            return BoardType.b3_corner_edge_adjacent_edge
                        if len(self.corners()) == 2:
                            return BoardType.b3_corner_edge_opposite_corner
                        return BoardType.b3_corner_edge_opposite_edge
                    if self.num_adjacent_corners() == 1:
                        return BoardType.b3_adjacent_corners_opposite_edge
                    return BoardType.b3_adjacent_edges_opposite_corner
                return BoardType.b3_only_corners
            return BoardType.b3_only_edges

        # 4
        if n == 4:
            if self.has_center():
                if self.num_adjacent_corners_edges() == 2:
                    return BoardType.b4_center_square
                if self.num_adjacent_corners_edges() == 1:
                    if self.num_adjacent_edges() == 1:
                        return BoardType.b4_center_z
                    return BoardType.b4_center_corners
                if self.num_adjacent_corners() == 1:
                    return BoardType.b4_center_t
                return BoardType.b4_center_edges
            if self.has_corner():
                if self.num_adjacent_corners() == 4:
                    return BoardType.b4_corners
                if self.num_adjacent_corners() == 2:
                    return BoardType.b4_corners_single_edge
                if self.num_adjacent_corners() == 1:
                    if self.num_adjacent_corners_edges() == 2:
                        return BoardType.b4_opposite_adjacent_corner_edges
                    return BoardType.b4_adjacent_corner_edge_adjacent_corner_adjacent_edge
                if self.num_adjacent_corners_edges() == 2:
                    if self.num_adjacent_edges() == 2:
                        return BoardType.b4_edges_3_l
                    if self.num_adjacent_edges() == 1:
                        if self.has_l():
                            return BoardType.b4_arrow
                        return BoardType.b4_spread_corner
                    return BoardType.b4_open_z
                return BoardType.b4_edges_3_no_l
            return BoardType.b4_edges

        # 5
        if n == 5:
            if self.has_center():
                return BoardType.b5_center
            if self.num_adjacent_edges() == 4:
                return BoardType.b5_edges
            if self.num_adjacent_edges() == 2:
                if self.num_adjacent_corners() == 1:
                    return BoardType.b5_v
                return BoardType.b5_hook
            return BoardType.b5_bow

        if n == 6:
            return BoardType.b6
        return BoardType.b_identity
