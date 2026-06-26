# calculator/pkg/calculator.py

from collections.abc import Callable
import functools

class Calculator:
    def __init__(self) -> None:
        self.operators: dict[str, Callable[[float, float], float]] = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: a / b,
            "^": lambda a, b: a ** b,  # Added exponentiation
        }
        self.precedence: dict[str, int] = {
            "+": 1,
            "-": 1,
            "*": 2,
            "/": 2,
            "^": 3,  # Higher precedence for exponentiation
        }

    def evaluate(self, expression: str) -> float | None:
        if not expression or expression.isspace():
            return None
        # Tokenize the expression, splitting by spaces and preserving parentheses
        tokens = []
        current_token = ""
        for char in expression:
            if char in "() ":
                if current_token:
                    tokens.append(current_token)
                    current_token = ""
                if char != " ": # Don't add spaces as tokens
                    tokens.append(char)
            else:
                current_token += char
        if current_token:
            tokens.append(current_token)

        return self._evaluate_infix(tokens)

    def _evaluate_infix(self, tokens: list[str]) -> float:
        values: list[float] = []
        operators: list[str] = []

        for token in tokens:
            if token == "(":
                operators.append(token)
            elif token == ")":
                while operators and operators[-1] != "(":
                    self._apply_operator(operators, values)
                if not operators or operators[-1] != "(":
                    raise ValueError("mismatched parentheses")
                operators.pop()  # Pop the "("
            elif token in self.operators:
                while (
                    operators
                    and operators[-1] in self.operators
                    and self.precedence.get(operators[-1], 0) >= self.precedence[token]
                ):
                    self._apply_operator(operators, values)
                operators.append(token)
            else:
                try:
                    values.append(float(token))
                except ValueError:
                    raise ValueError(f"invalid token: {token}")

        while operators:
            if operators[-1] == "(":
                raise ValueError("mismatched parentheses")
            self._apply_operator(operators, values)

        if len(values) != 1:
            raise ValueError("invalid expression")

        return values[0]

    def _apply_operator(self, operators: list[str], values: list[float]) -> None:
        if not operators:
            return

        operator = operators.pop()
        if len(values) < 2:
            raise ValueError(f"not enough operands for operator {operator}")

        b = values.pop()
        a = values.pop()
        values.append(self.operators[operator](a, b))