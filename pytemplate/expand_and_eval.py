# pylint:disable=eval-used

"""
expand_and_evaluate
"""

from typing import Set


QUOTE: str = '"'
BOOLEAN_STRING_SET: Set = {"True", "False"}


def get_evaluated_value(value: str):
    """get_evaluated_value"""

    if value == "AAA":
        return "x"

    if value == "BBB":
        return "y"

    if value == "CCC":
        return "z"

    return None


def expand_expression_recursively(expression):
    """expand_expression_recursively"""

    [left, operator_symbol, right] = expression
    result = False
    get_result = True

    if isinstance(left, list):
        left, recursion_result = expand_expression_recursively(left)
        result = result or recursion_result

    if isinstance(right, list):
        right, recursion_result = expand_expression_recursively(right)
        result = result or recursion_result

    if isinstance(left, str):
        if not left in BOOLEAN_STRING_SET:
            evaluated_value = get_evaluated_value(left)

            if evaluated_value is None:
                get_result = False
            else:
                result = True
                left = evaluated_value

    return [left, operator_symbol, right, get_result], result


def evaluate_expression_recursively(expression):
    """evaluate_expression_recursively"""

    [left, operator_symbol, right, result] = expression

    if isinstance(left, list):
        left, recursion_result = evaluate_expression_recursively(left)
        result = result and recursion_result

    if isinstance(right, list):
        right, recursion_result = evaluate_expression_recursively(right)
        result = result and recursion_result

    if result:
        if not left in BOOLEAN_STRING_SET:
            left = QUOTE + left + QUOTE

        if not right in BOOLEAN_STRING_SET:
            right = QUOTE + right + QUOTE

        expression = str(eval(" ".join([left, operator_symbol, right])))
    else:
        expression = [left, operator_symbol, right]

    return expression, result


if __name__ == "__main__":
    expr = [
        ["AAA", "==", "a"],
        "and",
        [["BBB", "==", "b"], "or", ["CCC", "!=", "c"]],
    ]

    expanded, expand_result = expand_expression_recursively(expr)
    print(f"expanded: {expanded}")
    print(f"expand_result: {expand_result}\n")

    answer, evaluate_result = evaluate_expression_recursively(expanded)
    print(f"answer: {answer}")
    print(f"evaluate_result: {evaluate_result}\n")

    print("-" * 80)

    expr = ["True", "and", ["True", "or", ["CCC", "!=", "c"]]]

    expanded, expand_result = expand_expression_recursively(expr)
    print(f"expanded: {expanded}")
    print(f"expand_result: {expand_result}\n")

    answer, evaluate_result = evaluate_expression_recursively(expanded)
    print(f"answer: {answer}")
    print(f"evaluate_result: {evaluate_result}\n")

    print("-" * 80)

    expr = [
        "True",
        "and",
        [["BBB", "==", "b"], "or", ["CCC", "!=", "c"]],
    ]

    expanded, expand_result = expand_expression_recursively(expr)
    print(f"expanded: {expanded}")
    print(f"expand_result: {expand_result}\n")

    answer, evaluate_result = evaluate_expression_recursively(expanded)
    print(f"answer: {answer}")
    print(f"evaluate_result: {evaluate_result}\n")

    print("-" * 80)

    expr = [
        ["AAA", "==", "a"],
        "and",
        ["True", "or", ["CCC", "!=", "c"]],
    ]

    expanded, expand_result = expand_expression_recursively(expr)
    print(f"expanded: {expanded}")
    print(f"expand_result: {expand_result}\n")

    answer, evaluate_result = evaluate_expression_recursively(expanded)
    print(f"answer: {answer}")
    print(f"evaluate_result: {evaluate_result}\n")

    print("-" * 80)

    expr = [["AAA", "==", "a"], "and", "True"]

    expanded, expand_result = expand_expression_recursively(expr)
    print(f"expanded: {expanded}")
    print(f"expand_result: {expand_result}\n")

    answer, evaluate_result = evaluate_expression_recursively(expanded)
    print(f"answer: {answer}")
    print(f"evaluate_result: {evaluate_result}\n")
