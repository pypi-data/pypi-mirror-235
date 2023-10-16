from typing import TypeVar, Generic, Optional

from PyCSPSolver.constraint import Constraint

V = TypeVar("V")
D = TypeVar("D")


class CSP(Generic[V, D]):
    """
    Generic class for representing a constraint satisfaction problem (CSP) and solving it with backtracking methods.

    Args:
        _variables (list[V]): list of variables
        _domains (dict[V, list[D]]): contains the domain values for each variable
    """

    def __init__(self, variables: list[V], domains: dict[V, list[D]]):
        self._variables: list[V] = variables
        self._domains: dict[V, list[D]] = domains
        self._constraints: dict[V, list[Constraint[V, D]]] = {variable: [] for variable in self._variables}

        # Check that each variable is in the domain
        for variable in variables:
            if variable not in domains:
                # Case: Variable not founded
                raise AttributeError("#ERROR_CSP: Each variable should have a list of domains!")

    def _get_unassigned(self, assignment: dict[V, D]) -> list[V]:
        """
        Returns the variables, that are not assigned, given the assignment.

        Args:
            assignment (dict[V, D]): mapping between variables and domain value

        Returns:
            list[V]: list of unassigned variables
        """
        return [variable for variable in self._variables if variable not in assignment]

    def _consistent(self, variable: V, assignment: dict[V, D]) -> bool:
        """
        Returns True if all constraints holds true for the given variable in assignment.

        Args:
            variable (V): variable to check if the constraints holds true
            assignment (dict[V, D]): mapping between variables and domain value

        Returns:
            bool: True if all constraints holds true
        """
        for constraint in self._constraints[variable]:
            if not constraint.satisfied(assignment):
                return False
        return True

    def add_constraint(self, constraint: Constraint[V, D]):
        """
        Adds a new constraint to the Constraint Satisfaction Problem (CSP).

        Args:
            constraint (Constraint[V, D]): new constraint to add to the CSP
        """
        for variable in constraint.get_variables():
            if variable in self._variables:
                # Case: Variable founded
                self._constraints[variable] += [constraint]
            else:
                # Case: Variable not founded
                raise AttributeError("#ERROR_CSP: Not all variables in constraint are given in the CSP!")

    def add_constraints(self, constraints: list[Constraint[V, D]]):
        """
        Adds a new constraint to the Constraint Satisfaction Problem (CSP).

        Args:
            constraints (list[Constraint[V, D]]): new constraints to add to the CSP
        """
        for constraint in constraints:
            self.add_constraint(constraint)


    def backtracking_search(self, assignment: dict[V, D] = {}) -> Optional[dict[V, D]]:
        """
        Simple backtracking search to solve a constraint satisfaction problem (CSP), where we want to assign each variable
        a domain value, that fulfills all given constraints. If there is no solution possible it will return None.

        Args:
            assignment (dict[V, D]): mapping between variables and domain value

        Returns:
            Optional[dict[V, D]]: solution of the constraint satisfaction problem (CSP)
        """
        # Check if every variable has a domain
        if len(self._variables) == len(assignment):
            return assignment

        # Get all variables that has no domain
        unassigned = self._get_unassigned(assignment)

        # Assign the first variable a domain
        variable = unassigned[0]
        for domain in self._domains[variable]:
            # Assign the value to the variable
            new_assignment = assignment.copy()
            new_assignment[variable] = domain

            # Check if we are consistent
            if self._consistent(variable, new_assignment):
                result = self.backtracking_search(new_assignment)
                if result is not None:
                    return result
        return None
