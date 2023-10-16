# PyCSPSolver
PyCSPSolver is a simple Python Framework for solving Constraint Satisfaction Problems (CSPs). 
You can find more information about CSPs
[here](https://en.wikipedia.org/wiki/Constraint_satisfaction_problem).

### Solving CSPs with PyCSPSolver
In the following, we want to solve a 2x2 sudoku puzzle with PyCSPSolver.
First we need to define our problem as CSP.
So we have to define variables, domains and constraints before we can solve it.

Each tile of the 2x2 sudoku board represents a variable Xi:
```python
"""
Our 2x2 sudoku board:
-----------------
|X1 |X2 |X3 |X4 |
|X5 |X6 |X7 |X8 |
|X9 |X10|X11|X12|
|X13|X14|X15|X16|
-----------------
"""
variables = ["X1", "X2", "X3", "X4", "X5", "X6", "X7", "X8", "X9", "X10", "X11", "X12", "X13", "X14", "X15", "X16"]
```

The possible values for each tile represents our domain:
```python
"""
Our domain for each X_i:
D = {1, 2, 3, 4}
"""
domains = {
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
```

Now we have to define the constraints.
PyCSPSolver has in principal four different types of constraints.

| Type of Constraint     | Explanation                                | Example  |
|:-----------------------|:-------------------------------------------|:---------|
| EqualToConstraint()    | variables should be equal to a value X     | X1 = 1   |
| EqualConstraint()      | variables should have an equal value       | X1 = X2  | 
| NotEqualToConstraint() | variables should be not equal to a value X | X1 != 1  |
| NotEqualConstraint()   | variables should have not an equal value   | X1 != X2 |

The following shows how to define the constraints from the example:

```python
from PyCSPSolver.constraint import EqualToConstraint, EqualConstraint, NotEqualToConstraint, NotEqualConstraint

constraint1 = EqualToConstraint(["X1"], 1)
constraint2 = EqualConstraint(["X1", "X2"])
constraint3 = NotEqualToConstraint(["X1"], 1)
constraint4 = NotEqualConstraint(["X1", "X2"])
```

With that in mind, we can now define the constraints of the 2x2 sudoku board, which are represented by the rules of 
sudoku.
The sudoku rules are that in each row, column or 2x2 square each value should only exist once.
The following shows the constraint of the 2x2 sudoku board:

```python
from PyCSPSolver.constraint import NotEqualConstraint

row1 = NotEqualConstraint(["X1", "X2", "X3", "X4"])
row2 = NotEqualConstraint(["X5", "X6", "X7", "X8"])
row3 = NotEqualConstraint(["X9", "X10", "X11", "X12"])
row4 = NotEqualConstraint(["X13", "X14", "X15", "X16"])
col1 = NotEqualConstraint(["X1", "X5", "X9", "X13"])
col2 = NotEqualConstraint(["X2", "X6", "X10", "X14"])
col3 = NotEqualConstraint(["X3", "X7", "X11", "X15"])
col4 = NotEqualConstraint(["X4", "X8", "X12", "X16"])
square1 = NotEqualConstraint(["X1", "X2", "X5", "X6"])
square2 = NotEqualConstraint(["X3", "X4", "X7", "X8"])
square3 = NotEqualConstraint(["X9", "X10", "X13", "X14"])
square4 = NotEqualConstraint(["X11", "X12", "X15", "X16"])
```

Now we have defined our 2x2 sudoku board as a CSP.
With all combined, we can now solve the CSP with PyCSPSolver.
The following code shows how to solve the CSP with simple backtracking search:

```python
from PyCSPSolver.csp import CSP

csp = CSP[str, int](variables=variables, domains=domains)

# Add the constraints to the CSP problem
csp.add_constraints([row1, row2, row3, row4])
csp.add_constraints([col1, col2, col3, col4])
csp.add_constraints([square1, square2, square3, square4])

# Solve the CSP with backtracking search
result = csp.backtracking_search()
print(result)
```


