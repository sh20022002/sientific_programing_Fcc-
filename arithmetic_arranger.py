def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    arranged_problems = []
    max_operand_width = 0

    for problem in problems:
        operator_index = problem.find("+") if "+" in problem else problem.find("-")

        if operator_index == -1:
            return "Error: Operator must be '+' or '-'."

        operand1 = problem[:operator_index].strip()
        operator = problem[operator_index]
        operand2 = problem[operator_index + 1:].strip()

        if not operand1.isdigit() or not operand2.isdigit():
            return "Error: Numbers must only contain digits."

        result = str(int(operand1) + int(operand2)) if operator == '+' else str(int(operand1) - int(operand2))

        max_operand_width = max(max_operand_width, len(operand1), len(operand2))
        arranged_problems.append((operand1, operator, operand2, result))

    lines = ["", "", "", ""]
    for operand1, operator, operand2, result in arranged_problems:
        lines[0] += operand1.rjust(max_operand_width + 2) + '    '
        lines[1] += operator + operand2.rjust(max_operand_width + 1) + '    '
        lines[2] += '-' * (max_operand_width + 2) + '    '
        lines[3] += result.rjust(max_operand_width + 2) + '    '

    arranged_problems = '\n'.join(line.rstrip() for line in lines)
    if show_answers:
        arranged_problems += '\n' + lines[3].rstrip()

    return arranged_problems

# Example usage:
problems = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
result = arithmetic_arranger(problems, True)
l = 0
while l <= 4:
    for line in result:
        print(line)
        l += 1