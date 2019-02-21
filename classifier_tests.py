import unittest
from classifier import Classifier, BoardType


class MockBoard():
    def __init__(self):
        self.cells = [0 for _ in range(9)]


class TestClassifier(unittest.TestCase):
    def setUp(self):
        self.classifier = Classifier(MockBoard())

    # test if empty board has no edges, corners or center
    def test_empty(self):
        self.classifier.board.cells = [0 for _ in range(9)]

        self.assertEqual(True, self.classifier.empty())
        self.assertEqual(False, self.classifier.has_center())
        self.assertEqual(False, self.classifier.has_edge())
        self.assertEqual(False, self.classifier.has_corner())

    # test corners()
    def test_corners(self):
        self.classifier.board.cells = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.assertEqual([], self.classifier.corners())

        self.classifier.board.cells = [1, 0, 0, 0, 0, 0, 0, 0, 0]
        self.assertEqual([1], self.classifier.corners())

        self.classifier.board.cells = [0, 0, 1, 0, 0, 0, 0, 0, 0]
        self.assertEqual([2], self.classifier.corners())

        self.classifier.board.cells = [0, 0, 0, 0, 0, 0, 0, 0, 1]
        self.assertEqual([3], self.classifier.corners(), )

        self.classifier.board.cells = [0, 0, 0, 0, 0, 0, 1, 0, 0]
        self.assertEqual([4], self.classifier.corners())

        self.classifier.board.cells = [1, 0, 1, 0, 0, 0, 0, 0, 0]
        self.assertEqual([1, 2], self.classifier.corners())

        self.classifier.board.cells = [1, 0, 0, 0, 0, 0, 0, 0, 1]
        self.assertEqual([1, 3], self.classifier.corners())

        self.classifier.board.cells = [1, 0, 0, 0, 0, 0, 1, 0, 0]
        self.assertEqual([1, 4], self.classifier.corners())

        self.classifier.board.cells = [0, 0, 1, 0, 0, 0, 0, 0, 1]
        self.assertEqual([2, 3], self.classifier.corners())

        self.classifier.board.cells = [0, 0, 1, 0, 0, 0, 1, 0, 0]
        self.assertEqual([2, 4], self.classifier.corners())

        self.classifier.board.cells = [0, 0, 0, 0, 0, 0, 1, 0, 1]
        self.assertEqual([3, 4], self.classifier.corners())

        self.classifier.board.cells = [1, 0, 1, 0, 0, 0, 1, 0, 0]
        self.assertEqual([1, 2, 4], self.classifier.corners())

        self.classifier.board.cells = [1, 0, 1, 0, 0, 0, 0, 0, 1]
        self.assertEqual([1, 2, 3], self.classifier.corners())

        self.classifier.board.cells = [1, 0, 0, 0, 0, 0, 1, 0, 1]
        self.assertEqual([1, 3, 4], self.classifier.corners())

        self.classifier.board.cells = [0, 0, 1, 0, 0, 0, 1, 0, 1]
        self.assertEqual([2, 3, 4], self.classifier.corners())

        self.classifier.board.cells = [1, 0, 1, 0, 0, 0, 1, 0, 1]
        self.assertEqual([1, 2, 3, 4], self.classifier.corners())

    # test edges()
    def test_edges(self):
        self.classifier.board.cells = [0, 1, 0, 0, 0, 0, 0, 0, 0]
        self.assertEqual([1], self.classifier.edges())

        self.classifier.board.cells = [0, 0, 0, 0, 0, 1, 0, 0, 0]
        self.assertEqual([2], self.classifier.edges())

        self.classifier.board.cells = [0, 0, 0, 0, 0, 0, 0, 1, 0]
        self.assertEqual([3], self.classifier.edges())

        self.classifier.board.cells = [0, 0, 0, 1, 0, 0, 0, 0, 0]
        self.assertEqual([4], self.classifier.edges())

        self.classifier.board.cells = [0, 1, 0, 0, 0, 1, 0, 0, 0]
        self.assertEqual([1, 2], self.classifier.edges())

        self.classifier.board.cells = [0, 1, 0, 0, 0, 0, 0, 1, 0]
        self.assertEqual([1, 3], self.classifier.edges())

        self.classifier.board.cells = [0, 1, 0, 1, 0, 0, 0, 0, 0]
        self.assertEqual([1, 4], self.classifier.edges())

        self.classifier.board.cells = [0, 0, 0, 0, 0, 1, 0, 1, 0]
        self.assertEqual([2, 3], self.classifier.edges())

        self.classifier.board.cells = [0, 0, 0, 1, 0, 1, 0, 0, 0]
        self.assertEqual([2, 4], self.classifier.edges())

        self.classifier.board.cells = [0, 0, 0, 1, 0, 0, 0, 1, 0]
        self.assertEqual([3, 4], self.classifier.edges())

        self.classifier.board.cells = [0, 1, 0, 0, 0, 1, 0, 1, 0]
        self.assertEqual([1, 2, 3], self.classifier.edges())

        self.classifier.board.cells = [0, 1, 0, 1, 0, 1, 0, 0, 0]
        self.assertEqual([1, 2, 4], self.classifier.edges())

        self.classifier.board.cells = [0, 1, 0, 1, 0, 0, 0, 1, 0]
        self.assertEqual([1, 3, 4], self.classifier.edges())

        self.classifier.board.cells = [0, 0, 0, 1, 0, 1, 0, 1, 0]
        self.assertEqual([2, 3, 4], self.classifier.edges())

        self.classifier.board.cells = [0, 1, 0, 1, 0, 1, 0, 1, 0]
        self.assertEqual([1, 2, 3, 4], self.classifier.edges())

    # test number of adjacent corners
    def test_adjacent_corners(self):
        self.classifier.board.cells = [1, 0, 0,
                                       0, 0, 0,
                                       0, 0, 1]
        self.assertEqual(0, self.classifier.num_adjacent_corners())

        self.classifier.board.cells = [1, 0, 0,
                                       0, 0, 0,
                                       1, 0, 1]
        self.assertEqual(2, self.classifier.num_adjacent_corners())

        self.classifier.board.cells = [1, 0, 1,
                                       0, 0, 0,
                                       1, 0, 1]
        self.assertEqual(4, self.classifier.num_adjacent_corners())

    # test number of adjacent edges
    def test_adjacent_edges(self):
        self.classifier.board.cells = [0, 1, 0,
                                       0, 0, 0,
                                       0, 1, 0]
        self.assertEqual(0, self.classifier.num_adjacent_edges())

        self.classifier.board.cells = [0, 1, 0,
                                       1, 0, 0,
                                       0, 0, 0]
        self.assertEqual(1, self.classifier.num_adjacent_edges())

        self.classifier.board.cells = [1, 1, 1,
                                       1, 0, 1,
                                       1, 0, 1]
        self.assertEqual(2, self.classifier.num_adjacent_edges())

        self.classifier.board.cells = [1, 1, 1,
                                       1, 1, 1,
                                       1, 1, 1]
        self.assertEqual(4, self.classifier.num_adjacent_edges())

    # test number of adjacent corners and edges
    def test_adjacent_corners_edges(self):
        self.classifier.board.cells = [0, 0, 0,
                                       0, 0, 0,
                                       0, 0, 0]
        self.assertEqual(0, self.classifier.num_adjacent_corners_edges())

        self.classifier.board.cells = [1, 1, 0,
                                       0, 0, 0,
                                       0, 0, 0]
        self.assertEqual(1, self.classifier.num_adjacent_corners_edges())

        self.classifier.board.cells = [0, 1, 1,
                                       1, 0, 0,
                                       0, 0, 0]
        self.assertEqual(1, self.classifier.num_adjacent_corners_edges())

        self.classifier.board.cells = [0, 1, 1,
                                       1, 0, 0,
                                       1, 0, 0]
        self.assertEqual(2, self.classifier.num_adjacent_corners_edges())

        self.classifier.board.cells = [0, 1, 1,
                                       1, 0, 0,
                                       1, 1, 0]
        self.assertEqual(3, self.classifier.num_adjacent_corners_edges())

        self.classifier.board.cells = [1, 1, 1,
                                       1, 0, 0,
                                       0, 1, 1]
        self.assertEqual(4, self.classifier.num_adjacent_corners_edges())

        self.classifier.board.cells = [1, 1, 1,
                                       1, 0, 1,
                                       1, 1, 0]
        self.assertEqual(6, self.classifier.num_adjacent_corners_edges())

        self.classifier.board.cells = [1, 1, 1,
                                       1, 0, 1,
                                       1, 1, 1]
        self.assertEqual(8, self.classifier.num_adjacent_corners_edges())

    # classify empty boards
    def test_classifier_0(self):
        self.classifier.board.cells = [0 for _ in range(9)]
        self.assertEqual(BoardType.b0_empty, self.classifier.classify())

    # classify boards with 1 cell
    def test_classifier_1(self):
        self.classifier.board.cells = [0 for _ in range(9)]
        self.classifier.board.cells[0] = 1
        self.assertEqual(BoardType.b1_corner, self.classifier.classify())

        self.classifier.board.cells = [0 for _ in range(9)]
        self.classifier.board.cells[2] = 1
        self.assertEqual(BoardType.b1_corner, self.classifier.classify())

        self.classifier.board.cells = [0 for _ in range(9)]
        self.classifier.board.cells[6] = 1
        self.assertEqual(BoardType.b1_corner, self.classifier.classify())

        self.classifier.board.cells = [0 for _ in range(9)]
        self.classifier.board.cells[8] = 1
        self.assertEqual(BoardType.b1_corner, self.classifier.classify())

        self.classifier.board.cells = [0 for _ in range(9)]
        self.classifier.board.cells[1] = 1
        self.assertEqual(BoardType.b1_edge, self.classifier.classify())

        self.classifier.board.cells = [0 for _ in range(9)]
        self.classifier.board.cells[3] = 1
        self.assertEqual(BoardType.b1_edge, self.classifier.classify())

        self.classifier.board.cells = [0 for _ in range(9)]
        self.classifier.board.cells[5] = 1
        self.assertEqual(BoardType.b1_edge, self.classifier.classify())

        self.classifier.board.cells = [0 for _ in range(9)]
        self.classifier.board.cells[7] = 1
        self.assertEqual(BoardType.b1_edge, self.classifier.classify())

        self.classifier.board.cells = [0 for _ in range(9)]
        self.classifier.board.cells[4] = 1
        self.assertEqual(BoardType.b1_center, self.classifier.classify())

    # classify boards with 2 cells with adjacent corner and edge
    def test_classifier_2_adjacent_corner_edge(self):
        self.classifier.board.cells = [1, 1, 0,
                                       0, 0, 0,
                                       0, 0, 0]
        self.assertEqual(BoardType.b2_adjacent_corner_edge, self.classifier.classify())

        self.classifier.board.cells = [1, 0, 0,
                                       1, 0, 0,
                                       0, 0, 0]
        self.assertEqual(BoardType.b2_adjacent_corner_edge, self.classifier.classify())

        self.classifier.board.cells = [0, 1, 1,
                                       0, 0, 0,
                                       0, 0, 0]
        self.assertEqual(BoardType.b2_adjacent_corner_edge, self.classifier.classify())

        self.classifier.board.cells = [0, 0, 1,
                                       0, 0, 1,
                                       0, 0, 0]
        self.assertEqual(BoardType.b2_adjacent_corner_edge, self.classifier.classify())

        self.classifier.board.cells = [0, 0, 0,
                                       0, 0, 1,
                                       0, 0, 1]
        self.assertEqual(BoardType.b2_adjacent_corner_edge, self.classifier.classify())

        self.classifier.board.cells = [0, 0, 0,
                                       0, 0, 0,
                                       0, 1, 1]
        self.assertEqual(BoardType.b2_adjacent_corner_edge, self.classifier.classify())

        self.classifier.board.cells = [0, 0, 0,
                                       0, 0, 0,
                                       1, 1, 0]
        self.assertEqual(BoardType.b2_adjacent_corner_edge, self.classifier.classify())

        self.classifier.board.cells = [0, 0, 0,
                                       1, 0, 0,
                                       1, 0, 0]
        self.assertEqual(BoardType.b2_adjacent_corner_edge, self.classifier.classify())

    # classify boards with 2 cells with adjacent corners
    def test_classifier_2_adjacent_corners(self):
        self.classifier.board.cells = [1, 0, 1,
                                       0, 0, 0,
                                       0, 0, 0]
        self.assertEqual(BoardType.b2_adjacent_corner, self.classifier.classify())

        self.classifier.board.cells = [0, 0, 1,
                                       0, 0, 0,
                                       0, 0, 1]
        self.assertEqual(BoardType.b2_adjacent_corner, self.classifier.classify())

        self.classifier.board.cells = [0, 0, 0,
                                       0, 0, 0,
                                       1, 0, 1]
        self.assertEqual(BoardType.b2_adjacent_corner, self.classifier.classify())

        self.classifier.board.cells = [1, 0, 0,
                                       0, 0, 0,
                                       1, 0, 0]
        self.assertEqual(BoardType.b2_adjacent_corner, self.classifier.classify())

    # classify boards with 2 cells with center and corner
    def test_classifier_2_center_corner(self):
        self.classifier.board.cells = [1, 0, 0,
                                       0, 1, 0,
                                       0, 0, 0]
        self.assertEqual(BoardType.b2_corner_center, self.classifier.classify())

        self.classifier.board.cells = [0, 0, 1,
                                       0, 1, 0,
                                       0, 0, 0]
        self.assertEqual(BoardType.b2_corner_center, self.classifier.classify())

        self.classifier.board.cells = [0, 0, 0,
                                       0, 1, 0,
                                       0, 0, 1]
        self.assertEqual(BoardType.b2_corner_center, self.classifier.classify())

        self.classifier.board.cells = [0, 0, 0,
                                       0, 1, 0,
                                       1, 0, 0]
        self.assertEqual(BoardType.b2_corner_center, self.classifier.classify())

    # classify boards with 2 cells with opposite edge and corner
    def test_classifier_2_opposite_corner_edge(self):
        self.classifier.board.cells = [1, 0, 0,
                                       0, 0, 1,
                                       0, 0, 0]
        self.assertEqual(BoardType.b2_opposite_corner_edge, self.classifier.classify())

        self.classifier.board.cells = [1, 0, 0,
                                       0, 0, 0,
                                       0, 1, 0]
        self.assertEqual(BoardType.b2_opposite_corner_edge, self.classifier.classify())

        self.classifier.board.cells = [0, 0, 1,
                                       0, 0, 0,
                                       0, 1, 0]
        self.assertEqual(BoardType.b2_opposite_corner_edge, self.classifier.classify())

        self.classifier.board.cells = [0, 0, 1,
                                       1, 0, 0,
                                       0, 0, 0]
        self.assertEqual(BoardType.b2_opposite_corner_edge, self.classifier.classify())

        self.classifier.board.cells = [0, 0, 0,
                                       1, 0, 0,
                                       0, 0, 1]
        self.assertEqual(BoardType.b2_opposite_corner_edge, self.classifier.classify())

        self.classifier.board.cells = [0, 1, 0,
                                       0, 0, 0,
                                       0, 0, 1]
        self.assertEqual(BoardType.b2_opposite_corner_edge, self.classifier.classify())

        self.classifier.board.cells = [0, 1, 0,
                                       0, 0, 0,
                                       1, 0, 0]
        self.assertEqual(BoardType.b2_opposite_corner_edge, self.classifier.classify())

        self.classifier.board.cells = [0, 0, 0,
                                       0, 0, 1,
                                       1, 0, 0]
        self.assertEqual(BoardType.b2_opposite_corner_edge, self.classifier.classify())

    # classify boards with 2 cells with opposite corners
    def test_classifier_2_opposite_corners(self):
        self.classifier.board.cells = [1, 0, 0,
                                       0, 0, 0,
                                       0, 0, 1]
        self.assertEqual(BoardType.b2_opposite_corner, self.classifier.classify())

        self.classifier.board.cells = [0, 0, 1,
                                       0, 0, 0,
                                       1, 0, 0]
        self.assertEqual(BoardType.b2_opposite_corner, self.classifier.classify())

    # classify boards with 2 cells with adjacent edges
    def test_classifier_2_adjacent_edges(self):
        self.classifier.board.cells = [0, 1, 0,
                                       0, 0, 1,
                                       0, 0, 0]
        self.assertEqual(BoardType.b2_adjacent_edge, self.classifier.classify())

        self.classifier.board.cells = [0, 0, 0,
                                       0, 0, 1,
                                       0, 1, 0]
        self.assertEqual(BoardType.b2_adjacent_edge, self.classifier.classify())

        self.classifier.board.cells = [0, 0, 0,
                                       1, 0, 0,
                                       0, 1, 0]
        self.assertEqual(BoardType.b2_adjacent_edge, self.classifier.classify())

        self.classifier.board.cells = [0, 1, 0,
                                       1, 0, 0,
                                       0, 0, 0]
        self.assertEqual(BoardType.b2_adjacent_edge, self.classifier.classify())

    # classify boards with 2 cells with center and edge
    def test_classifier_2_center_edge(self):
        self.classifier.board.cells = [0, 1, 0,
                                       0, 1, 0,
                                       0, 0, 0]
        self.assertEqual(BoardType.b2_edge_center, self.classifier.classify())

        self.classifier.board.cells = [0, 0, 0,
                                       0, 1, 1,
                                       0, 0, 0]
        self.assertEqual(BoardType.b2_edge_center, self.classifier.classify())

        self.classifier.board.cells = [0, 0, 0,
                                       0, 1, 0,
                                       0, 1, 0]
        self.assertEqual(BoardType.b2_edge_center, self.classifier.classify())

        self.classifier.board.cells = [0, 0, 0,
                                       1, 1, 0,
                                       0, 0, 0]
        self.assertEqual(BoardType.b2_edge_center, self.classifier.classify())

    # classify boards with 2 cells with opposite edges
    def test_classifier_2_opposite_edges(self):
        self.classifier.board.cells = [0, 1, 0,
                                       0, 0, 0,
                                       0, 1, 0]
        self.assertEqual(BoardType.b2_opposite_edge, self.classifier.classify())

        self.classifier.board.cells = [0, 0, 0,
                                       1, 0, 1,
                                       0, 0, 0]
        self.assertEqual(BoardType.b2_opposite_edge, self.classifier.classify())

    # classify boards with 3 cells with center
    def test_classifier_3_center(self):
        self.classifier.board.cells = [0, 1, 0,
                                       0, 1, 1,
                                       0, 0, 0]
        self.assertEqual(BoardType.b3_center_edge, self.classifier.classify())

        self.classifier.board.cells = [0, 0, 0,
                                       0, 1, 1,
                                       0, 1, 0]
        self.assertEqual(BoardType.b3_center_edge, self.classifier.classify())

        self.classifier.board.cells = [0, 0, 0,
                                       1, 1, 0,
                                       0, 1, 0]
        self.assertEqual(BoardType.b3_center_edge, self.classifier.classify())

        self.classifier.board.cells = [0, 1, 0,
                                       1, 1, 0,
                                       0, 0, 0]
        self.assertEqual(BoardType.b3_center_edge, self.classifier.classify())

        self.classifier.board.cells = [1, 0, 1,
                                       0, 1, 0,
                                       0, 0, 0]
        self.assertEqual(BoardType.b3_center_corner, self.classifier.classify())

        self.classifier.board.cells = [0, 0, 1,
                                       0, 1, 0,
                                       0, 0, 1]
        self.assertEqual(BoardType.b3_center_corner, self.classifier.classify())

        self.classifier.board.cells = [0, 0, 0,
                                       0, 1, 0,
                                       1, 0, 1]
        self.assertEqual(BoardType.b3_center_corner, self.classifier.classify())

        self.classifier.board.cells = [1, 0, 0,
                                       0, 1, 0,
                                       1, 0, 0]
        self.assertEqual(BoardType.b3_center_corner, self.classifier.classify())

        self.classifier.board.cells = [1, 1, 0,
                                       0, 1, 0,
                                       0, 0, 0]
        self.assertEqual(BoardType.b3_center_adjacent_corner_edge, self.classifier.classify())

        self.classifier.board.cells = [0, 1, 1,
                                       0, 1, 0,
                                       0, 0, 0]
        self.assertEqual(BoardType.b3_center_adjacent_corner_edge, self.classifier.classify())

        self.classifier.board.cells = [0, 0, 1,
                                       0, 1, 1,
                                       0, 0, 0]
        self.assertEqual(BoardType.b3_center_adjacent_corner_edge, self.classifier.classify())

        self.classifier.board.cells = [0, 0, 0,
                                       0, 1, 1,
                                       0, 0, 1]
        self.assertEqual(BoardType.b3_center_adjacent_corner_edge, self.classifier.classify())

        self.classifier.board.cells = [0, 0, 0,
                                       0, 1, 0,
                                       0, 1, 1]
        self.assertEqual(BoardType.b3_center_adjacent_corner_edge, self.classifier.classify())

        self.classifier.board.cells = [0, 0, 0,
                                       0, 1, 0,
                                       1, 1, 0]
        self.assertEqual(BoardType.b3_center_adjacent_corner_edge, self.classifier.classify())

        self.classifier.board.cells = [0, 0, 0,
                                       1, 1, 0,
                                       1, 0, 0]
        self.assertEqual(BoardType.b3_center_adjacent_corner_edge, self.classifier.classify())

        self.classifier.board.cells = [1, 0, 0,
                                       1, 1, 0,
                                       0, 0, 0]
        self.assertEqual(BoardType.b3_center_adjacent_corner_edge, self.classifier.classify())

        self.classifier.board.cells = [1, 0, 0,
                                       0, 1, 1,
                                       0, 0, 0]
        self.assertEqual(BoardType.b3_center_opposite_corner_edge, self.classifier.classify())

        self.classifier.board.cells = [0, 0, 0,
                                       0, 1, 1,
                                       1, 0, 0]
        self.assertEqual(BoardType.b3_center_opposite_corner_edge, self.classifier.classify())

        self.classifier.board.cells = [1, 0, 0,
                                       0, 1, 0,
                                       0, 1, 0]
        self.assertEqual(BoardType.b3_center_opposite_corner_edge, self.classifier.classify())

        self.classifier.board.cells = [0, 0, 1,
                                       0, 1, 0,
                                       0, 1, 0]
        self.assertEqual(BoardType.b3_center_opposite_corner_edge, self.classifier.classify())

        self.classifier.board.cells = [0, 0, 0,
                                       1, 1, 0,
                                       0, 0, 1]
        self.assertEqual(BoardType.b3_center_opposite_corner_edge, self.classifier.classify())

        self.classifier.board.cells = [0, 0, 1,
                                       1, 1, 0,
                                       0, 0, 0]
        self.assertEqual(BoardType.b3_center_opposite_corner_edge, self.classifier.classify())

        self.classifier.board.cells = [0, 1, 0,
                                       0, 1, 0,
                                       0, 0, 1]
        self.assertEqual(BoardType.b3_center_opposite_corner_edge, self.classifier.classify())

        self.classifier.board.cells = [0, 1, 0,
                                       0, 1, 0,
                                       1, 0, 0]
        self.assertEqual(BoardType.b3_center_opposite_corner_edge, self.classifier.classify())

    # classify board with 3 cells with corner
    def test_classifier_3_corner(self):
        self.classifier.board.cells = [1, 1, 0,
                                       1, 0, 0,
                                       0, 0, 0]
        self.assertEqual(BoardType.b3_corner, self.classifier.classify())

        self.classifier.board.cells = [0, 1, 1,
                                       0, 0, 1,
                                       0, 0, 0]
        self.assertEqual(BoardType.b3_corner, self.classifier.classify())

        self.classifier.board.cells = [0, 0, 0,
                                       1, 0, 0,
                                       1, 1, 0]
        self.assertEqual(BoardType.b3_corner, self.classifier.classify())

        self.classifier.board.cells = [0, 0, 0,
                                       0, 0, 1,
                                       0, 1, 1]
        self.assertEqual(BoardType.b3_corner, self.classifier.classify())

    # classify board with 3 cells with only edges
    def test_classifier_3_only_edges(self):
        self.classifier.board.cells = [0, 1, 0,
                                       1, 0, 1,
                                       0, 0, 0]
        self.assertEqual(BoardType.b3_only_edges, self.classifier.classify())

        self.classifier.board.cells = [0, 1, 0,
                                       1, 0, 0,
                                       0, 1, 0]
        self.assertEqual(BoardType.b3_only_edges, self.classifier.classify())

        self.classifier.board.cells = [0, 1, 0,
                                       0, 0, 1,
                                       0, 1, 0]
        self.assertEqual(BoardType.b3_only_edges, self.classifier.classify())

        self.classifier.board.cells = [0, 0, 0,
                                       1, 0, 1,
                                       0, 1, 0]
        self.assertEqual(BoardType.b3_only_edges, self.classifier.classify())

    # classify board with 3 cells with only corners
    def test_classifier_3_only_corners(self):
        self.classifier.board.cells = [1, 0, 1,
                                       0, 0, 0,
                                       0, 0, 1]
        self.assertEqual(BoardType.b3_only_corners, self.classifier.classify())

        self.classifier.board.cells = [1, 0, 1,
                                       0, 0, 0,
                                       1, 0, 0]
        self.assertEqual(BoardType.b3_only_corners, self.classifier.classify())

        self.classifier.board.cells = [1, 0, 0,
                                       0, 0, 0,
                                       1, 0, 1]
        self.assertEqual(BoardType.b3_only_corners, self.classifier.classify())

        self.classifier.board.cells = [0, 0, 1,
                                       0, 0, 0,
                                       1, 0, 1]
        self.assertEqual(BoardType.b3_only_corners, self.classifier.classify())

    # classify board with 3 cells with only adjacent corners and opposite edge
    def test_classifier_3_adjacent_corners_opposite_edge(self):
        self.classifier.board.cells = [1, 0, 1,
                                       0, 0, 0,
                                       0, 1, 0]
        self.assertEqual(BoardType.b3_adjacent_corners_opposite_edge, self.classifier.classify())

        self.classifier.board.cells = [1, 0, 0,
                                       0, 0, 1,
                                       1, 0, 0]
        self.assertEqual(BoardType.b3_adjacent_corners_opposite_edge, self.classifier.classify())

        self.classifier.board.cells = [0, 1, 0,
                                       0, 0, 0,
                                       1, 0, 1]
        self.assertEqual(BoardType.b3_adjacent_corners_opposite_edge, self.classifier.classify())

        self.classifier.board.cells = [0, 0, 1,
                                       1, 0, 0,
                                       0, 0, 1]
        self.assertEqual(BoardType.b3_adjacent_corners_opposite_edge, self.classifier.classify())

    # classify board with 3 cells with only adjacent edges and opposite corner
    def test_classifier_3_adjacent_edges_opposite_corner(self):
        self.classifier.board.cells = [1, 0, 0,
                                       0, 0, 1,
                                       0, 1, 0]
        self.assertEqual(BoardType.b3_adjacent_edges_opposite_corner, self.classifier.classify())

        self.classifier.board.cells = [0, 0, 1,
                                       1, 0, 0,
                                       0, 1, 0]
        self.assertEqual(BoardType.b3_adjacent_edges_opposite_corner, self.classifier.classify())

        self.classifier.board.cells = [0, 1, 0,
                                       1, 0, 0,
                                       0, 0, 1]
        self.assertEqual(BoardType.b3_adjacent_edges_opposite_corner, self.classifier.classify())

        self.classifier.board.cells = [0, 1, 0,
                                       0, 0, 1,
                                       1, 0, 0]
        self.assertEqual(BoardType.b3_adjacent_edges_opposite_corner, self.classifier.classify())

    # classify board with 3 cells with only 1 adjacent corner and edge and adjacent edge
    def test_classifier_3_corner_edge_adjacent_edge(self):
        self.classifier.board.cells = [1, 1, 0,
                                       0, 0, 1,
                                       0, 0, 0]
        self.assertEqual(BoardType.b3_corner_edge_adjacent_edge, self.classifier.classify())

        self.classifier.board.cells = [0, 1, 1,
                                       1, 0, 0,
                                       0, 0, 0]
        self.assertEqual(BoardType.b3_corner_edge_adjacent_edge, self.classifier.classify())

        self.classifier.board.cells = [0, 0, 1,
                                       0, 0, 1,
                                       0, 1, 0]
        self.assertEqual(BoardType.b3_corner_edge_adjacent_edge, self.classifier.classify())

        self.classifier.board.cells = [0, 1, 0,
                                       0, 0, 1,
                                       0, 0, 1]
        self.assertEqual(BoardType.b3_corner_edge_adjacent_edge, self.classifier.classify())

        self.classifier.board.cells = [0, 0, 0,
                                       1, 0, 0,
                                       0, 1, 1]
        self.assertEqual(BoardType.b3_corner_edge_adjacent_edge, self.classifier.classify())

        self.classifier.board.cells = [0, 0, 0,
                                       0, 0, 1,
                                       1, 1, 0]
        self.assertEqual(BoardType.b3_corner_edge_adjacent_edge, self.classifier.classify())

        self.classifier.board.cells = [0, 1, 0,
                                       1, 0, 0,
                                       1, 0, 0]
        self.assertEqual(BoardType.b3_corner_edge_adjacent_edge, self.classifier.classify())

        self.classifier.board.cells = [1, 0, 0,
                                       1, 0, 0,
                                       0, 1, 0]
        self.assertEqual(BoardType.b3_corner_edge_adjacent_edge, self.classifier.classify())

    # classify board with 3 cells with only 1 adjacent corner and edge and opposite edge
    def test_classifier_3_corner_edge_opposite_edge(self):
        self.classifier.board.cells = [1, 1, 0,
                                       0, 0, 0,
                                       0, 1, 0]
        self.assertEqual(BoardType.b3_corner_edge_opposite_edge, self.classifier.classify())

        self.classifier.board.cells = [0, 1, 1,
                                       0, 0, 0,
                                       0, 1, 0]
        self.assertEqual(BoardType.b3_corner_edge_opposite_edge, self.classifier.classify())

        self.classifier.board.cells = [0, 0, 1,
                                       1, 0, 1,
                                       0, 0, 0]
        self.assertEqual(BoardType.b3_corner_edge_opposite_edge, self.classifier.classify())

        self.classifier.board.cells = [0, 0, 0,
                                       1, 0, 1,
                                       0, 0, 1]
        self.assertEqual(BoardType.b3_corner_edge_opposite_edge, self.classifier.classify())

        self.classifier.board.cells = [0, 1, 0,
                                       0, 0, 0,
                                       0, 1, 1]
        self.assertEqual(BoardType.b3_corner_edge_opposite_edge, self.classifier.classify())

        self.classifier.board.cells = [0, 1, 0,
                                       0, 0, 0,
                                       1, 1, 0]
        self.assertEqual(BoardType.b3_corner_edge_opposite_edge, self.classifier.classify())

        self.classifier.board.cells = [0, 0, 0,
                                       1, 0, 1,
                                       1, 0, 0]
        self.assertEqual(BoardType.b3_corner_edge_opposite_edge, self.classifier.classify())

        self.classifier.board.cells = [1, 0, 0,
                                       1, 0, 1,
                                       0, 0, 0]
        self.assertEqual(BoardType.b3_corner_edge_opposite_edge, self.classifier.classify())

    # classify board with 3 cells with only 1 adjacent corner and edge and adjacent corner
    def test_classifier_3_corner_edge_adjacent_corner(self):
        self.classifier.board.cells = [1, 1, 0,
                                       0, 0, 0,
                                       1, 0, 0]
        self.assertEqual(BoardType.b3_corner_edge_adjacent_corner, self.classifier.classify())

        self.classifier.board.cells = [0, 1, 1,
                                       0, 0, 0,
                                       0, 0, 1]
        self.assertEqual(BoardType.b3_corner_edge_adjacent_corner, self.classifier.classify())

        self.classifier.board.cells = [1, 0, 1,
                                       0, 0, 1,
                                       0, 0, 0]
        self.assertEqual(BoardType.b3_corner_edge_adjacent_corner, self.classifier.classify())

        self.classifier.board.cells = [0, 0, 0,
                                       0, 0, 1,
                                       1, 0, 1]
        self.assertEqual(BoardType.b3_corner_edge_adjacent_corner, self.classifier.classify())

        self.classifier.board.cells = [0, 0, 1,
                                       0, 0, 0,
                                       0, 1, 1]
        self.assertEqual(BoardType.b3_corner_edge_adjacent_corner, self.classifier.classify())

        self.classifier.board.cells = [1, 0, 0,
                                       0, 0, 0,
                                       1, 1, 0]
        self.assertEqual(BoardType.b3_corner_edge_adjacent_corner, self.classifier.classify())

        self.classifier.board.cells = [0, 0, 0,
                                       1, 0, 0,
                                       1, 0, 1]
        self.assertEqual(BoardType.b3_corner_edge_adjacent_corner, self.classifier.classify())

        self.classifier.board.cells = [1, 0, 1,
                                       1, 0, 0,
                                       0, 0, 0]
        self.assertEqual(BoardType.b3_corner_edge_adjacent_corner, self.classifier.classify())

    # classify board with 3 cells with only 1 adjacent corner and edge and opposite corner
    def test_classifier_3_corner_edge_opposite_corner(self):
        self.classifier.board.cells = [1, 1, 0,
                                       0, 0, 0,
                                       0, 0, 1]
        self.assertEqual(BoardType.b3_corner_edge_opposite_corner, self.classifier.classify())

        self.classifier.board.cells = [0, 1, 1,
                                       0, 0, 0,
                                       1, 0, 0]
        self.assertEqual(BoardType.b3_corner_edge_opposite_corner, self.classifier.classify())

        self.classifier.board.cells = [0, 0, 1,
                                       0, 0, 1,
                                       1, 0, 0]
        self.assertEqual(BoardType.b3_corner_edge_opposite_corner, self.classifier.classify())

        self.classifier.board.cells = [1, 0, 0,
                                       0, 0, 1,
                                       0, 0, 1]
        self.assertEqual(BoardType.b3_corner_edge_opposite_corner, self.classifier.classify())

        self.classifier.board.cells = [0, 0, 1,
                                       0, 0, 0,
                                       1, 1, 0]
        self.assertEqual(BoardType.b3_corner_edge_opposite_corner, self.classifier.classify())

        self.classifier.board.cells = [1, 0, 0,
                                       0, 0, 0,
                                       0, 1, 1]
        self.assertEqual(BoardType.b3_corner_edge_opposite_corner, self.classifier.classify())

        self.classifier.board.cells = [1, 0, 0,
                                       1, 0, 0,
                                       0, 0, 1]
        self.assertEqual(BoardType.b3_corner_edge_opposite_corner, self.classifier.classify())

        self.classifier.board.cells = [0, 0, 1,
                                       1, 0, 0,
                                       1, 0, 0]
        self.assertEqual(BoardType.b3_corner_edge_opposite_corner, self.classifier.classify())


if __name__ == '__main__':
    unittest.main()