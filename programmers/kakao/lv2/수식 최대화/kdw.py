from itertools import permutations


def str_to_list(expression, operators):
    result, operand = [], ''

    for o in expression:
        if o not in operators:
            operand += o
        else:
            result += [int(operand), o]
            operand = ''

    result.append(int(operand))

    return result


def calculate(expression, permutation):
    stack = expression

    for operator in permutation:
        expression, stack = stack, [None]

        for o in expression:
            if stack[-1] == operator:
                stack.pop()
                if operator == '+':
                    stack[-1] += o
                elif operator == '-':
                    stack[-1] -= o
                else:
                    stack[-1] *= o
            else:
                stack.append(o)

    return stack.pop()


def solution(expression):
    answer = 0

    operators = {operator for operator in ['+', '-', '*']
                 if expression.find(operator) != -1}

    expression = str_to_list(expression, operators)

    for permutation in permutations(operators):
        answer = max(answer, abs(calculate(expression, permutation)))

    return answer
