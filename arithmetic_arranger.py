import re


def arithmetic_arranger(problems, calc=False):
    
    if len(problems) > 5:
        return 'Error: Too many problems.'
    
    lin1 = ''
    lin2 = ''
    lin3 = ''
    lin4 = ''

    for problem in problems:
        lin = construct_func(problem)

        if lin.__contains__('Error'):
            return lin

        lin1 = lin1 + f'{lin[0]}'
        lin2 = lin2 + f'{lin[1]}'
        lin3 = lin3 + f'{lin[2]}'
        lin4 = lin4 + f'{lin[3]}'

    if calc is False:
        return f'{lin1.rstrip()}\n{lin2.rstrip()}\n{lin3.rstrip()}'.rstrip()
    else:
        return f'{lin1.rstrip()}\n{lin2.rstrip()}\n{lin3.rstrip()}\n{lin4.rstrip()}'.rstrip()


def construct_func(problem):
    cut = problem.split()
    if problem.find("+") == -1 and problem.find("-") == -1:
        return "Error: Operator must be '+' or '-'."

    if bool(re.match('^[0-9]+$', cut[0])) is False or bool(re.match('^[0-9]+$', cut[2])) is False:
        return "Error: Numbers must only contain digits."

    else:
        num1 = int(cut[0])
        op = problem.split()[1]
        num2 = int(cut[2])

        if len(cut[0]) > 4 or len(cut[2]) > 4:
            return "Error: Numbers cannot be more than four digits."

    return construct_cont(num1, num2, op)


def construct_cont(num1, num2, op):
    size = max(len(str(num1)), len(str(num2))) + 2
    total = num1 + num2 if op == "+" else num1 - num2

    line1 = ((size - len(str(num1))) * ' ') + str(num1)
    line2 = ((size - len(str(num2))) * ' ') + str(num2)
    line3 = size * '-'
    line4 = ((size - len(str(total))) * ' ') + str(total)

    line2 = line2[:0] + op + line2[0+1:]

    return [line1 + (4 * ' '), line2 + (4 * ' '), line3 + (4 * ' '), line4 + (4 * ' ')]
