# pylint:disable=eval-used

"""
expand_and_eval
"""

QUOTE: str = '"'


def get_evaluated_value(value: str):
    """get_evaluated_value"""

    if value == "AAA":
        return "a"

    if value == "BBB":
        return "x"

    if value == "CCC":
        return "c"

    return None


def expand_expression(expression):
    """expand_expression"""

    [left, operator_symbol, right] = expression
    boolean_string_set = {"True", "False"}
    result = False
    get_result = True

    if isinstance(left, list):
        left, recursion_result = expand_expression(left)
        result = result or recursion_result
    else:
        if not left in boolean_string_set:
            evaluated_value = get_evaluated_value(left)

            if evaluated_value is None:
                get_result = False
            else:
                result = True
                left = evaluated_value

    if isinstance(right, list):
        right, recursion_result = expand_expression(right)
        result = result or recursion_result

    return [left, operator_symbol, right, get_result], result


def evaluate_expression(expression):
    """evaluate_expression"""

    [left, operator_symbol, right, result] = expression

    if isinstance(left, list):
        left, recursion_result = evaluate_expression(left)
        result = result and recursion_result

    if isinstance(right, list):
        right, recursion_result = evaluate_expression(right)
        result = result and recursion_result

    if result:
        expression = " ".join(
            [QUOTE + left + QUOTE, operator_symbol, QUOTE + right + QUOTE]
        )
        return str(eval(expression)), True
    else:
        expression = [left, operator_symbol, right]
        return expression, False


if __name__ == "__main__":
    expr_tree = [
        ["AAA", "==", "a"],
        "and",
        [["BBB", "==", "b"], "or", ["CCC", "!=", "c"]],
    ]

    expanded_expr_tree, expand_result = expand_expression(expr_tree)
    print(f"expanded_expr_tree: {expanded_expr_tree}")
    print(f"expand_result: {expand_result}\n")

    answer, evaluate_result = evaluate_expression(expanded_expr_tree)
    print(f"answer: {answer}")
    print(f"evaluate_result: {evaluate_result}\n")

    print("-" * 80)

    answer_tree = ["True", "and", ["True", "or", ["CCC", "!=", "c"]]]

    expanded_expr_tree, expand_result = expand_expression(answer_tree)
    print(f"expanded_expr_tree: {expanded_expr_tree}")
    print(f"expand_result: {expand_result}\n")

    answer, evaluate_result = evaluate_expression(expanded_expr_tree)
    print(f"answer: {answer}")
    print(f"evaluate_result: {evaluate_result}\n")

    print("-" * 80)

    answer_tree = [
        "True",
        "and",
        [["BBB", "==", "b"], "or", ["CCC", "!=", "c"]],
    ]

    expanded_expr_tree, expand_result = expand_expression(answer_tree)
    print(f"expanded_expr_tree: {expanded_expr_tree}")
    print(f"expand_result: {expand_result}\n")

    answer, evaluate_result = evaluate_expression(expanded_expr_tree)
    print(f"answer: {answer}")
    print(f"evaluate_result: {evaluate_result}\n")

    print("-" * 80)

    answer_tree = [
        ["AAA", "==", "a"],
        "and",
        ["True", "or", ["CCC", "!=", "c"]],
    ]

    expanded_expr_tree, expand_result = expand_expression(answer_tree)
    print(f"expanded_expr_tree: {expanded_expr_tree}")
    print(f"expand_result: {expand_result}\n")

    answer, evaluate_result = evaluate_expression(expanded_expr_tree)
    print(f"answer: {answer}")
    print(f"evaluate_result: {evaluate_result}\n")

    print("-" * 80)

    answer_tree = [["AAA", "==", "a"], "and", "True"]

    expanded_expr_tree, expand_result = expand_expression(answer_tree)
    print(f"expanded_expr_tree: {expanded_expr_tree}")
    print(f"expand_result: {expand_result}\n")

    answer, evaluate_result = evaluate_expression(expanded_expr_tree)
    print(f"answer: {answer}")
    print(f"evaluate_result: {evaluate_result}\n")
