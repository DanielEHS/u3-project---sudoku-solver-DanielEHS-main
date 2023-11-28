from unittest import TestCase
from sudoku_solver import SudokuSolver

class SudokuSolverTests(TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def _assert_puzzle(self, result, answer):
        for i in range(len(answer)):
            for j in range(len(answer)):
                self.assertEqual(result[i][j],  answer[i][j])

    def test_easy_4x4(self):
        puzzle = [["A", "B", "C", "D"],
                 ["C", None, "A", "B"],
                 ["B", "A", "D", None],
                 ["D", None, "B", "A"]]

        answer = [["A", "B", "C", "D"],
                 ["C", "D", "A", "B"],
                 ["B", "A", "D", "C"],
                 ["D", "C", "B", "A"]]

        solver = SudokuSolver(["A", "B", "C", "D"])
        result = solver.solve(puzzle)
        self._assert_puzzle(result, answer)

    def test_hard_4x4(self):
        puzzle = [[None, "B", None, None],
                 ["C", None, None, "B"],
                 [None, "A", "D", None],
                 ["D", None, None, "A"]]

        answer = [["A", "B", "C", "D"],
                 ["C", "D", "A", "B"],
                 ["B", "A", "D", "C"],
                 ["D", "C", "B", "A"]]

        solver = SudokuSolver(["A", "B", "C", "D"])
        result = solver.solve(puzzle)
        self._assert_puzzle(result, answer)
    
    # Want a challenge? Uncomment this test out and see how well your solutions works.
    # This test case will require code optimized for being smarter about which spots to fill in 
    # first (rather than just in order of blank spots)
    # The record for a super optimized solution was under 1s. See how close you can get!
    def test_16x16_advanced(self):
        answer = [['5', 'B', 'C', '2', '7', '9', '1', '3', '4', '6', '8', 'E', 'A', 'D', 'F', 'G'], 
            ['4', 'G', '3', '9', '2', '5', 'F', '6', '7', 'A', 'C', 'D', '1', 'B', '8', 'E'], 
            ['F', '6', 'A', '7', 'D', 'B', 'E', '8', '2', 'G', '5', '1', '4', '3', '9', 'C'], 
            ['D', '1', 'E', '8', '4', 'A', 'C', 'G', 'B', '9', 'F', '3', '6', '7', '5', '2'], 
            ['A', 'C', 'B', '3', 'F', 'G', 'D', '1', '6', '2', '4', '9', '8', '5', 'E', '7'], 
            ['E', '9', 'G', '6', 'C', '2', 'B', 'A', 'D', '5', '7', '8', 'F', '1', '4', '3'], 
            ['8', '7', 'D', '5', '9', '4', '3', 'E', 'F', 'B', '1', 'G', '2', 'C', '6', 'A'], 
            ['1', '4', '2', 'F', '5', '6', '8', '7', '3', 'E', 'A', 'C', 'D', 'G', 'B', '9'], 
            ['G', 'E', '7', 'C', 'A', '3', '5', 'B', '1', '8', '2', '4', '9', '6', 'D', 'F'], 
            ['3', 'A', '9', 'D', '6', '1', 'G', '4', 'E', 'C', 'B', 'F', '5', '2', '7', '8'], 
            ['B', '8', '5', '4', 'E', '7', '2', 'F', 'G', 'D', '9', '6', '3', 'A', 'C', '1'], 
            ['2', 'F', '6', '1', '8', 'C', '9', 'D', '5', '7', '3', 'A', 'B', 'E', 'G', '4'], 
            ['6', '2', '1', 'B', 'G', 'E', '4', '9', '8', '3', 'D', '7', 'C', 'F', 'A', '5'], 
            ['7', '5', 'F', 'G', '1', '8', 'A', '2', 'C', '4', '6', 'B', 'E', '9', '3', 'D'], 
            ['9', 'D', '4', 'E', '3', 'F', '6', 'C', 'A', '1', 'G', '5', '7', '8', '2', 'B'], 
            ['C', '3', '8', 'A', 'B', 'D', '7', '5', '9', 'F', 'E', '2', 'G', '4', '1', '6']]
     
        puzzle = [["5", None, None, "2", "7", None, "1", None, None, "6", None, None, None, None, None, None],
            [None, "G", None, None, None, None, "F", "6", None, "A", None, None, None, "B", None, "E"],
            ["F", "6", None, None, "D", None, None, None, None, None, "5", None, None, "3", None, None],
            ["D", None, None, "8", None, "A", "C", None, None, "9", None, "3", None, None, "5", None],
            [None, None, "B", "3", "F", None, None, None, None, None, "4", None, "8", None, "E", "7"],
            ["E", None, None, None, "C", "2", "B", None, "D", None, None, None, "F", None, None, None],
            [None, "7", None, None, None, None, None, None, None, None, "1", None, None, "C", None, None],
            [None, "4", "2", None, "5", None, None, None, "3", "E", "A", "C", None, None, None, "9"],
            [None, "E", "7", "C", None, None, None, "B", None, None, None, None, None, "6", None, "F"],
            [None, "A", None, None, None, "1", "G", "4", None, None, None, None, None, "2", "7", None],
            ["B", None, "5", "4", "E", None, None, None, None, "D", None, "6", None, None, None, "1"],
            [None, "F", None, "1", "8", None, "9", None, None, "7", None, None, "B", None, None, "4"],
            [None, None, None, None, "G", None, "4", None, None, "3", None, "7", None, None, "A", None],
            [None, "5", None, None, None, "8", None, "2", "C", "4", None, None, "E", None, None, None],
            ["9", None, "4", None, None, None, None, "C", None, "1", None, "5", None, "8", None, None],
            [None, None, None, "A", "B", "D", "7", None, "9", None, None, None, None, "4", None, "6"]]
        solver = SudokuSolver(["A", "B", "C", "D", "E", "F", "G", "1", "2", "3", "4", "5", "6", "7", "8", "9"])
        result = solver.solve(puzzle)
        self._assert_puzzle(result, answer)
