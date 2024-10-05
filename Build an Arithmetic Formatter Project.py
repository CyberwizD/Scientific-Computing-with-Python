''' Build an Arithmetric Formatter Project '''

def arithmetic_arranger(problems, show_results=False):
    # Check if there are too many problems to solve
    if len(problems) > 5:
        return "Error: Too many problems."

    # Create an empty lists to store the parts of each problem
    first_operands = []  # List to store the top numbers
    second_operands = []  # List to store the bottom numbers
    operators = []  # List to store the operators (+ or -)

    # Split each problem into its parts
    for problem in problems:
        # Check if the problem has "+" or "-"
        if "+" in problem:
            operands = problem.split(" + ")  # Split the problem at " + "
            operators.append("+")  # Remember that the operator is "+"
        elif "-" in problem:
            operands = problem.split(" - ")  # Split the problem at " - "
            operators.append("-")  # Remember that the operator is "-"
        else:
            # If the problem has a different operator, return an error
            return "Error: Operator must be '+' or '-'."

        # Check if the operands are all digits (no letters or symbols)
        if not (operands[0].isdigit() and operands[1].isdigit()):
            return "Error: Numbers must only contain digits."

        # Check if the operands are too big (more than four digits)
        if len(operands[0]) > 4 or len(operands[1]) > 4:
            return "Error: Numbers cannot be more than four digits."

        # Add the top and bottom numbers to their respective lists
        first_operands.append(operands[0])
        second_operands.append(operands[1])

    # Create the lines that will hold the arranged problems
    line1 = ""  # The first line (top numbers)
    line2 = ""  # The second line (operators and bottom numbers)
    line3 = ""  # The third line (dashes)
    line4 = ""  # The fourth line (answers)

    # Formatting each problem to look nice
    for i in range(len(problems)):
        # Calculate how much space we need (width = longest number + 2 spaces)
        width = max(len(first_operands[i]), len(second_operands[i])) + 2

        # Add the top number to line 1, right-aligned to the width
        line1 += first_operands[i].rjust(width)

        # Add the operator and bottom number to line 2, with the operator in front
        line2 += operators[i] + second_operands[i].rjust(width - 1)

        # Add the dashes to line 3
        line3 += "-" * width

        # If we want to show the results
        if show_results:
            # Calculate the result of the problem (add or subtract)
            if operators[i] == "+":
                result = str(int(first_operands[i]) + int(second_operands[i]))
            else:
                result = str(int(first_operands[i]) - int(second_operands[i]))

            # Add the result to line 4, right-aligned to the width
            line4 += result.rjust(width)

        # Add spaces between problems, but not after the last problem
        if i < len(problems) - 1:
            line1 += "    "
            line2 += "    "
            line3 += "    "
            if show_results:
                line4 += "    "

    # Combine all the lines into the final arranged output
    arranged_problems = line1 + "\n" + line2 + "\n" + line3
    if show_results:
        arranged_problems += "\n" + line4

    # Return the final formatted string
    return arranged_problems

# Example usage of the function
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]), '\n')
print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))
