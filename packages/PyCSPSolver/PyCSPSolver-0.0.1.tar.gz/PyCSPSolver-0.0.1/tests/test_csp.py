import unittest

from PyCSPSolver.csp import CSP
from PyCSPSolver.constraint import NotEqualConstraint


class TestCSP(unittest.TestCase):
    """
    Tests the class CSP.
    """

    def setUp(self):
        """
        The following example shows how to solve a 2x2 sudoku, where each row, column, square only allows that the
        values D={1, 2, 3, 4} occurring once. The following shows how to represent a 2x2 sudoku board as a constraint-
        satisfaction problem (CSP):

        -----------------
        |X1 |X2 |X3 |X4 |
        |X5 |X6 |X7 |X8 |
        |X9 |X10|X11|X12|
        |X13|X14|X15|X16|
        -----------------

        Each variable X_i can have the following domain values: {1, 2, 3, 4}.
        The constraints are defined as follows:

        Constraints for the rows:
        - C1: X1 != X2 != X3 != X4
        - C2: X5 != X6 != X7 != X8
        - C3: X9 != X10 != X11 != X12
        - C4: X13 != X14 != X15 != X16

        Constraints for the columns:
        - C5: X1 != X5 != X9 != X13
        - C6: X2 != X6 != X10 != X14
        - C7: X3 != X7 != X11 != X15
        - C8: X4 != X8 != X12 != X16

        Constraints for the squares:
        - C9: X1 != X2 != X5 != X6
        - C10: X3 != X4 != X7 != X8
        - C11: X9 != X10 != X13 != X14
        - C12: X11 != X12 != X15 != X16
        """
        self.variables = ["X1", "X2", "X3", "X4", "X5", "X6", "X7", "X8", "X9",
                          "X10", "X11", "X12", "X13", "X14", "X15", "X16"]
        self.domains = {
            "X1": [1, 2, 3, 4],
            "X2": [1, 2, 3, 4],
            "X3": [1, 2, 3, 4],
            "X4": [1, 2, 3, 4],
            "X5": [1, 2, 3, 4],
            "X6": [1, 2, 3, 4],
            "X7": [1, 2, 3, 4],
            "X8": [1, 2, 3, 4],
            "X9": [1, 2, 3, 4],
            "X10": [1, 2, 3, 4],
            "X11": [1, 2, 3, 4],
            "X12": [1, 2, 3, 4],
            "X13": [1, 2, 3, 4],
            "X14": [1, 2, 3, 4],
            "X15": [1, 2, 3, 4],
            "X16": [1, 2, 3, 4],
        }

        self.csp = CSP[str, int](variables=self.variables, domains=self.domains)

        # Define row, column, square constraints
        self.row_c1 = NotEqualConstraint(["X1", "X2", "X3", "X4"])
        self.row_c2 = NotEqualConstraint(["X5", "X6", "X7", "X8"])
        self.row_c3 = NotEqualConstraint(["X9", "X10", "X11", "X12"])
        self.row_c4 = NotEqualConstraint(["X13", "X14", "X15", "X16"])
        self.col_c1 = NotEqualConstraint(["X1", "X5", "X9", "X13"])
        self.col_c2 = NotEqualConstraint(["X2", "X6", "X10", "X14"])
        self.col_c3 = NotEqualConstraint(["X3", "X7", "X11", "X15"])
        self.col_c4 = NotEqualConstraint(["X4", "X8", "X12", "X16"])
        self.square_c1 = NotEqualConstraint(["X1", "X2", "X5", "X6"])
        self.square_c2 = NotEqualConstraint(["X3", "X4", "X7", "X8"])
        self.square_c3 = NotEqualConstraint(["X9", "X10", "X13", "X14"])
        self.square_c4 = NotEqualConstraint(["X11", "X12", "X15", "X16"])

        # Add the constraints
        self.csp.add_constraints([self.row_c1, self.row_c2, self.row_c3, self.row_c4])
        self.csp.add_constraints([self.col_c1, self.col_c2, self.col_c3, self.col_c4])
        self.csp.add_constraints([self.square_c1, self.square_c2, self.square_c3, self.square_c4])

    def test_backtracking_search(self):
        """
        Tests the method backtracking_search().
        """
        expected = {'X1': 1, 'X2': 2, 'X3': 3, 'X4': 4,
                    'X5': 3, 'X6': 4, 'X7': 1, 'X8': 2,
                    'X9': 2, 'X10': 1, 'X11': 4, 'X12': 3,
                    'X13': 4, 'X14': 3, 'X15': 2, 'X16': 1}
        self.assertEqual(expected, self.csp.backtracking_search())


if __name__ == '__main__':
    unittest.main()
