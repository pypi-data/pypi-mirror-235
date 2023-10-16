import unittest

from PyCSPSolver.constraint import EqualToConstraint, EqualConstraint, NotEqualToConstraint, NotEqualConstraint


class TestEqualToConstraint(unittest.TestCase):
    """
    Tests the class EqualToConstraint.
    """

    def setUp(self):
        self.variables = ["X1", "X2", "X3", "X4"]
        self.domain = 1
        self.constraint = EqualToConstraint[str, int](self.variables, self.domain)

        self.valid_assignment1 = {"X1": 1, "X2": 1, "X3": 1, "X4": 1}
        self.valid_assignment2 = {"X1": 1, "X3": 1}
        self.valid_assignment3 = {}
        self.invalid_assignment1 = {"X1": 2, "X2": 2, "X3": 2, "X4": 2}
        self.invalid_assignment2 = {"X1": 1, "X4": 2}
        self.invalid_assignment3 = {"X2": 1, "X3": 2, "X4": 1}

    def test_get_variables(self):
        """
        Tests the method get_variables().
        """
        self.assertEqual(self.variables, self.constraint.get_variables())

    def test_satisfied(self):
        """
        Tests the method satisfied().
        """
        satisfied1 = self.constraint.satisfied(self.valid_assignment1)
        satisfied2 = self.constraint.satisfied(self.valid_assignment2)
        satisfied3 = self.constraint.satisfied(self.valid_assignment3)
        not_satisfied1 = self.constraint.satisfied(self.invalid_assignment1)
        not_satisfied2 = self.constraint.satisfied(self.invalid_assignment2)
        not_satisfied3 = self.constraint.satisfied(self.invalid_assignment3)

        self.assertTrue(satisfied1)
        self.assertTrue(satisfied2)
        self.assertTrue(satisfied3)
        self.assertFalse(not_satisfied1)
        self.assertFalse(not_satisfied2)
        self.assertFalse(not_satisfied3)

    def test_str(self):
        """
        Tests the magic method __str__().
        """
        expected = "Constraint: X1 = X2 = X3 = X4 = 1"
        self.assertEqual(expected, str(self.constraint))

    def test_repr(self):
        expected = "[EqualToConstraint(['X1', 'X2', 'X3', 'X4'], 1)]"
        self.assertEqual(expected, str([self.constraint]))


class TestEqualConstraint(unittest.TestCase):
    """
    Tests the class EqualConstraint.
    """

    def setUp(self):
        self.variables = ["X1", "X2", "X3", "X4"]
        self.constraint = EqualConstraint[str, int](self.variables)

        self.valid_assignment1 = {"X1": 1, "X2": 1, "X3": 1, "X4": 1}
        self.valid_assignment2 = {"X1": 1, "X3": 1}
        self.valid_assignment3 = {}
        self.invalid_assignment1 = {"X1": 1, "X2": 2, "X3": 2, "X4": 2}
        self.invalid_assignment2 = {"X1": 1, "X4": 2}
        self.invalid_assignment3 = {"X2": 1, "X3": 2, "X4": 1}

    def test_get_variables(self):
        """
        Tests the method get_variables().
        """
        self.assertEqual(self.variables, self.constraint.get_variables())

    def test_satisfied(self):
        """
        Tests the method satisfied().
        """
        satisfied1 = self.constraint.satisfied(self.valid_assignment1)
        satisfied2 = self.constraint.satisfied(self.valid_assignment2)
        satisfied3 = self.constraint.satisfied(self.valid_assignment3)
        not_satisfied1 = self.constraint.satisfied(self.invalid_assignment1)
        not_satisfied2 = self.constraint.satisfied(self.invalid_assignment2)
        not_satisfied3 = self.constraint.satisfied(self.invalid_assignment3)

        self.assertTrue(satisfied1)
        self.assertTrue(satisfied2)
        self.assertTrue(satisfied3)
        self.assertFalse(not_satisfied1)
        self.assertFalse(not_satisfied2)
        self.assertFalse(not_satisfied3)

    def test_str(self):
        """
        Tests the magic method __str__().
        """
        expected = "Constraint: X1 = X2 = X3 = X4"
        self.assertEqual(expected, str(self.constraint))

    def test_repr(self):
        expected = "[EqualConstraint(['X1', 'X2', 'X3', 'X4'])]"
        self.assertEqual(expected, str([self.constraint]))


class TestNotEqualToConstraint(unittest.TestCase):
    """
    Tests the class NotEqualToConstraint.
    """

    def setUp(self):
        self.variables = ["X1", "X2", "X3", "X4"]
        self.domain = 1
        self.constraint = NotEqualToConstraint[str, int](self.variables, self.domain)

        self.valid_assignment1 = {"X1": 2, "X2": 3, "X3": 4, "X4": 5}
        self.valid_assignment2 = {"X1": 2, "X4": 5}
        self.valid_assignment3 = {}

        self.invalid_assignment1 = {"X1": 1, "X2": 2, "X3": 3, "X4": 4}
        self.invalid_assignment2 = {"X1": 1, "X3": 3}
        self.invalid_assignment3 = {"X2": 1, "X3": 3, "X4": 4}

    def test_get_variables(self):
        """
        Tests the method get_variables().
        """
        self.assertEqual(self.variables, self.constraint.get_variables())

    def test_satisfied(self):
        """
        Tests the method satisfied().
        """
        satisfied1 = self.constraint.satisfied(self.valid_assignment1)
        satisfied2 = self.constraint.satisfied(self.valid_assignment2)
        satisfied3 = self.constraint.satisfied(self.valid_assignment3)
        not_satisfied1 = self.constraint.satisfied(self.invalid_assignment1)
        not_satisfied2 = self.constraint.satisfied(self.invalid_assignment2)
        not_satisfied3 = self.constraint.satisfied(self.invalid_assignment3)

        self.assertTrue(satisfied1)
        self.assertTrue(satisfied2)
        self.assertTrue(satisfied3)
        self.assertFalse(not_satisfied1)
        self.assertFalse(not_satisfied2)
        self.assertFalse(not_satisfied3)

    def test_str(self):
        """
        Tests the magic method __str__().
        """
        expected = "Constraint: X1 != 1, X2 != 1, X3 != 1, X4 != 1"
        self.assertEqual(expected, str(self.constraint))

    def test_repr(self):
        expected = "[NotEqualToConstraint(['X1', 'X2', 'X3', 'X4'], 1)]"
        self.assertEqual(expected, str([self.constraint]))


class TestNotEqualConstraint(unittest.TestCase):
    """
    Tests the class NotEqualConstraint.
    """

    def setUp(self):
        self.variables = ["X1", "X2", "X3", "X4"]
        self.constraint = NotEqualConstraint[str, int](self.variables)

        self.valid_assignment1 = {"X1": 1, "X2": 2, "X3": 3, "X4": 4}
        self.valid_assignment2 = {"X1": 1, "X4": 2}
        self.valid_assignment3 = {}

        self.invalid_assignment1 = {"X1": 1, "X2": 1, "X3": 3, "X4": 4}
        self.invalid_assignment2 = {"X1": 1, "X3": 1}
        self.invalid_assignment3 = {"X2": 1, "X3": 2, "X4": 1}

    def test_get_variables(self):
        """
        Tests the method get_variables().
        """
        self.assertEqual(self.variables, self.constraint.get_variables())

    def test_satisfied(self):
        """
        Tests the method satisfied().
        """
        satisfied1 = self.constraint.satisfied(self.valid_assignment1)
        satisfied2 = self.constraint.satisfied(self.valid_assignment2)
        satisfied3 = self.constraint.satisfied(self.valid_assignment3)
        not_satisfied1 = self.constraint.satisfied(self.invalid_assignment1)
        not_satisfied2 = self.constraint.satisfied(self.invalid_assignment2)
        not_satisfied3 = self.constraint.satisfied(self.invalid_assignment3)

        self.assertTrue(satisfied1)
        self.assertTrue(satisfied2)
        self.assertTrue(satisfied3)
        self.assertFalse(not_satisfied1)
        self.assertFalse(not_satisfied2)
        self.assertFalse(not_satisfied3)

    def test_str(self):
        """
        Tests the magic method __str__().
        """
        expected = "Constraint: X1 != X2 != X3 != X4"
        self.assertEqual(expected, str(self.constraint))

    def test_repr(self):
        expected = "[NotEqualConstraint(['X1', 'X2', 'X3', 'X4'])]"
        self.assertEqual(expected, str([self.constraint]))


if __name__ == '__main__':
    unittest.main()
