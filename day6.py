import re
import numpy as np
from functools import reduce
from collections import namedtuple

def get_inputs():
    with open("inputs/day6/real.txt") as f:
        lines = f.readlines()
        lines = [re.sub(r"[\s]+", " ", line.strip()) for line in lines]
        lines = [line.split(" ") for line in lines]
    return lines


def calculate_result(inputs):
    total = 0
    for row in inputs:
        numbers, operator = row[:-1], row[-1]
        if operator == "*":
            result = reduce(lambda x, y: int(x)*int(y), numbers)
        if operator == "+":
            result = reduce(lambda x, y: int(x)+int(y), numbers)
        # print(result)
        total += result
    print(total)


def part1():
    inputs = get_inputs()
    inputs = np.array(inputs).T.tolist()
    calculate_result(inputs)

# ====== part 2 ========

Calculation = namedtuple("Calculation", ["operator", "numbers"])

def get_inputs_part2():
    with open("inputs/day6/real.txt") as f:
        lines = f.readlines()
        lines = [[c for c in line.replace("\n", "")] for line in lines]
    lines = np.array(lines).T.tolist()
    lines.append([""])
    return lines

def parse_input(inputs: np.array):
    all_calculations = []
    current_numbers = []
    current_operator = ""
    for line in inputs:
        value = "".join(line)
        if value.strip() == "":
            # Build calculation
            all_calculations.append(
                Calculation(current_operator, current_numbers)
            )
            # Reset
            current_operator = ""
            current_numbers = []
            continue

        # An actual line
        if "*" in value:
            current_operator = "*"
        if "+" in value:
            current_operator = "+"
        value = value.replace("*", "").replace("+", "")
        current_numbers.append(int(value))
    return all_calculations

def calculate_results_part2(inputs: list[Calculation]):
    total = 0
    for item in inputs:
        if item.operator == "*":
            result = reduce(lambda x, y: x*y, item.numbers)
        if item.operator == "+":
            result = reduce(lambda x, y: x+y, item.numbers)
        print(f"{result=}, {item.operator=}, {item.numbers}")
        total += result
    return total

def part2():
    inputs = get_inputs_part2()
    inputs = parse_input(inputs)
    total = calculate_results_part2(inputs)
    print(total)

if __name__ == "__main__":
    # part1()
    part2()