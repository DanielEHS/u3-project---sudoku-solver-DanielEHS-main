from unittest import TestCase
from sudoku_solver import SudokuSolver

class SudokuSolverStudentTests(TestCase):
    def setUp(self) -> None:
        return super().setUp()
    
    def _assert_puzzle(self, result, answer):
        for i in range(len(answer)):
            for j in range(len(answer)):
                self.assertEqual(result[i][j],  answer[i][j])

    def test_student_helper_function_case(self): 
        solver = SudokuSolver(["1", "2", "3", "4", "5", "6", "7", "8", "9"])
        solver.size_root = 3
        result = solver.get_square(5, 6)
        self.assertEqual(result, 5)

    def test_student_9x9(self):
        puzzle = [[None, None, "7", None, None, None, None, "9", "8"],
                  [None, None, "3", None, None, None, None, None, None],
                  ["5", None, None, None, None, "6", None, None, None],
                  [None, None, None, None, None, None, "8", None, "6"],
                  [None, None, "5", None, None, None, "9", None, "3"],
                  [None, None, None, "3", "7", "2", "4", None, None],
                  ["7", None, "6", None, "1", "3", "5", None, None],
                  [None, "9", None, None, None, None, "7", "6", None],
                  [None, None, "4", "8", None, None, None, None, None]]
        
        answer = [["6", "4", "7", "2", "3", "5", "1", "9", "8"],
                  ["9", "1", "3", "7", "4", "8", "6", "5", "2"],
                  ["5", "8", "2", "1", "9", "6", "3", "4", "7"],
                  ["2", "3", "1", "4", "5", "9", "8", "7", "6"],
                  ["4", "7", "5", "6", "8", "1", "9", "2", "3"],
                  ["8", "6", "9", "3", "7", "2", "4", "1", "5"],
                  ["7", "2", "6", "9", "1", "3", "5", "8", "4"],
                  ["3", "9", "8", "5", "2", "4", "7", "6", "1"],
                  ["1", "5", "4", "8", "6", "7", "2", "3", "9"]]
        
        solver = SudokuSolver(["1", "2", "3", "4", "5", "6", "7", "8", "9"])
        result = solver.solve(puzzle)
        self._assert_puzzle(result, answer)
    
    def test_student_16x16(self):
        puzzle = [["B", None, "4", None, None, "9", None, "F", None, None, "6", None, "5", None, None, "E"],
                  [None, None, None, None, "C", None, None, None, "1", None, None, "B", "2", "0", None, "7"],
                  [None, "3", None, "5", "1", None, "6", None, None, None, None, None, None, "C", "F", "A"],
                  [None, None, None, None, "E", None, None, None, "2", "7", "5", None, None, None, "4", None],
                  [None, "D", "0", None, None, None, "9", None, None, None, None, "E", None, None, None, None],
                  ["E", None, None, None, None, "F", None, "4", None, None, None, None, "9", None, "1", None],
                  [None, None, "9", "8", "6", None, None, "C", None, None, "F", None, "0", "3", "E", "4"],
                  [None, "5", "2", None, "3", "E", "1", "D", None, "C", "8", None, "A", None, None, "6"],
                  ["0", None, None, "D", None, "8", "4", None, "A", "5", "2", "7", None, "6", "C", None],
                  ["3", "F", "A", "7", None, "6", None, None, "9", None, None, "C", "1", "4", None, None],
                  [None, "6", None, "C", None, None, None, None, "3", None, "D", None, None, None, None, "B"],
                  [None, None, None, None, "2", None, None, None, None, "6", None, None, None, "7", "A", None],
                  [None, "E", None, None, None, "3", "C", "9", None, None, None, "A", None, None, None, None],
                  ["1", "0", "5", None, None, None, None, None, None, "9", None, "3", "7", None, "B", None],
                  ["8", None, "D", "4", "B", None, None, "E", None, None, None, "5", None, None, None, None],
                  ["7", None, None, "9", None, "1", None, None, "E", None, "B", None, None, "5", None, "C"]]

        answer = [["B", "2", "4", "0", "7", "9", "8", "F", "C", "A", "6", "D", "5", "1", "3", "E"],
                  ["9", "8", "E", "A", "C", "4", "D", "5", "1", "F", "3", "B", "2", "0", "6", "7"],
                  ["D", "3", "7", "5", "1", "0", "6", "2", "4", "E", "9", "8", "B", "C", "F", "A"],
                  ["C", "1", "F", "6", "E", "A", "B", "3", "2", "7", "5", "0", "8", "9", "4", "D"],             
                  ["6", "D", "0", "1", "A", "B", "9", "7", "5", "3", "4", "E", "C", "F", "8", "2"],
                  ["E", "B", "C", "3", "8", "F", "0", "4", "7", "2", "A", "6", "9", "D", "1", "5"],
                  ["A", "7", "9", "8", "6", "5", "2", "C", "D", "B", "F", "1", "0", "3", "E", "4"],
                  ["4", "5", "2", "F", "3", "E", "1", "D", "0", "C", "8", "9", "A", "B", "7", "6"],
                  ["0", "9", "B", "D", "F", "8", "4", "1", "A", "5", "2", "7", "E", "6", "C", "3"],
                  ["3", "F", "A", "7", "D", "6", "5", "B", "9", "8", "E", "C", "1", "4", "2", "0"],
                  ["2", "6", "1", "C", "9", "7", "E", "A", "3", "0", "D", "4", "F", "8", "5", "B"],
                  ["5", "4", "8", "E", "2", "C", "3", "0", "B", "6", "1", "F", "D", "7", "A", "9"],
                  ["F", "E", "6", "B", "5", "3", "C", "9", "8", "D", "7", "A", "4", "2", "0", "1"],
                  ["1", "0", "5", "2", "4", "D", "A", "6", "F", "9", "C", "3", "7", "E", "B", "8"],
                  ["8", "C", "D", "4", "B", "2", "7", "E", "6", "1", "0", "5", "3", "A", "9", "F"],
                  ["7", "A", "3", "9", "0", "1", "F", "8", "E", "4", "B", "2", "6", "5", "D", "C"]]

        solver = SudokuSolver(["1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "0"])
        result = solver.solve(puzzle)
        self._assert_puzzle(result, answer)