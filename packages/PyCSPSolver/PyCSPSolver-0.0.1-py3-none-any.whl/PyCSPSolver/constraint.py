from typing import TypeVar, Generic
from abc import abstractmethod

V = TypeVar("V")
D = TypeVar("D")


class Constraint(Generic[V, D]):
    """
    Generic abstract class for representing a constraint for a Constraint Satisfaction Problem (CSP)

    Args:
        _variables (list[V]): list of variables
    """

    def __init__(self, variables: list[V]):
        assert len(variables) >= 1, "#ERROR_CONSTRAINT: variables should have at least 1 variable!"
        self._variables = variables

    def get_variables(self) -> list[V]:
        """
        Returns:
            list[V]: list of variables
        """
        return self._variables

    @abstractmethod
    def satisfied(self, assignment: dict[V, D]) -> bool:
        """
        Checks if the assignment of the variables (V) with the domains (D) does not violate the conditions.

        Args:
            assignment (dict[V, D]): mapping between variable and domain value
        
        Returns:
            bool: True, if all variables assigned with the domain fulfills the conditions
        """
        pass

    @abstractmethod
    def __str__(self) -> str:
        """
        Returns:
            str: String representation of the Constraint
        """
        pass

    @abstractmethod
    def __repr__(self) -> str:
        """
        Returns:
            str: Short string representation of the Constraint
        """
        pass


class EqualToConstraint(Constraint[V, D]):
    """
    Generic class for representing a constraint, where the given variables should be equal to a domain value.
    Let say that our condition is the following:
        - C := X1 = X2 = X3 = 1

    We can easily create this constraint by the following example code:
        - constraint = EqualToConstraint[str, int](["X1", "X2", "X3"], 1)

    Args:
        _variables (list[V]): list of variables
        _domain (D): domain value which should be equal to all given variables
    """

    def __init__(self, variables: list[V], domain: D):
        super().__init__(variables)
        self._domain = domain

    def satisfied(self, assignment: dict[V, D]) -> bool:
        """
        Checks if all given variables have the domain value (D) in the given assignment.

        Args:
            assignment (dict[V, D]): mapping between variable and domain value

        Returns:
            bool: True, if all variables assigned with the domain fulfills the condition
        """
        visited = {self._domain}
        for variable in self._variables:
            if variable in assignment and assignment[variable] not in visited:
                # Case: Found x-th variable which has a different value
                return False
        return True

    def __str__(self) -> str:
        text = f"Constraint: "
        for variable in self._variables:
            text += f"{str(variable)} = "
        text += str(self._domain)
        return text

    def __repr__(self) -> str:
        return f"EqualToConstraint({str(self._variables)}, {str(self._domain)})"


class EqualConstraint(Constraint[V, D]):
    """
    Generic class for representing a constraint, where each given variable should have the same domain value.
    Let say that our condition is the following:
        - C := X1 = X2 = X3

    We can easily create this constraint by the following example code:
        - constraint = EqualConstraint[str, int](["X1", "X2", "X3"])

    Args:
        _variables (list[V]): list of variables
        _domain (D): domain value which should be equal to all given variables
    """

    def satisfied(self, assignment: dict[V, D]) -> bool:
        """
        Checks if all given variables have the same domain value (D) in the given assignment.

        Args:
            assignment (dict[V, D]): mapping between variable and domain value

        Returns:
            bool: True, if all variables assigned with the domain fulfills the equal condition
        """
        visited = set()
        for variable in self._variables:
            if variable in assignment and len(visited) == 0:
                # Case: Found first variable
                visited.add(assignment[variable])
            elif variable in assignment and assignment[variable] not in visited:
                # Case: Found x-th variable which has a different value
                return False
        return True

    def __str__(self) -> str:
        text = f"Constraint: "
        for variable in self._variables:
            text += f"{str(variable)} = "
        text = text[:-3]
        return text

    def __repr__(self) -> str:
        return f"EqualConstraint({str(self._variables)})"


class NotEqualToConstraint(Constraint[V, D]):
    """
    Generic class for representing a constraint, where the given variables should be not equal to a domain value.
    Let say that or condition is the following:
        - C := X1 != 1, X2 != 1, X3 != 1

    We can easily create this constraint by the following example code:
        - constraint = NotEqualToConstraint[str, int](["X1", "X2", "X3"], 1)

    Args:
        _variables (list[V]): list of variables
        _domain (D): domain value which should be unequal to all given variables
    """

    def __init__(self, variables: list[V], domain: D):
        super().__init__(variables)
        self._domain = domain

    def satisfied(self, assignment: dict[V, D]) -> bool:
        """
        Checks if all given variables do not have the domain value (D) in the given assignment.

        Args:
            assignment (dict[V, D]): mapping between variable and domain value

        Returns:
            bool: True, if all variables assigned with the domain fulfills the condition
        """
        visited = {self._domain}
        for variable in self._variables:
            if variable in assignment and assignment[variable] in visited:
                # Case: Found x-th variable which has the same value
                return False
        return True

    def __str__(self) -> str:
        text = f"Constraint: "
        for variable in self._variables:
            text += f"{str(variable)} != {str(self._domain)}, "
        text = text[:-2]
        return text

    def __repr__(self) -> str:
        return f"NotEqualToConstraint({str(self._variables)}, {str(self._domain)})"


class NotEqualConstraint(Constraint[V, D]):
    """
    Generic class for representing a constraint, where each given variable should not have the same domain value.
    Let say that our condition is the following:
        - C := X1 != X2 != X3

    We can easily create this constraint by the following example code:
        - constraint = NotEqualConstraint[str, int](["X1", "X2", "X3"])

    Args:
        _variables (list[V]): list of variables
        _domain (D): domain value which should be equal to all given variables
    """

    def satisfied(self, assignment: dict[V, D]) -> bool:
        """
        Checks if all given variables have the different domain value (D) in the given assignment.

        Args:
            assignment (dict[V, D]): mapping between variable and domain value

        Returns:
            bool: True, if all variables assigned with the domain fulfills the not-equal condition
        """
        visited = set()
        for variable in self._variables:
            if variable in assignment and assignment[variable] in visited:
                # Case: Found duplicated domain value
                return False
            elif variable in assignment:
                # Case: Found non-duplicated domain value
                visited.add(assignment[variable])
        return True

    def __str__(self) -> str:
        text = f"Constraint: "
        for variable in self._variables:
            text += f"{str(variable)} != "
        text = text[:-4]
        return text

    def __repr__(self) -> str:
        return f"NotEqualConstraint({str(self._variables)})"
