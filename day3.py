
def get_inputs():
    with open("inputs/day3/real.txt") as f:
        lines = f.readlines()
        lines = [[int(c) for c in line.strip()] for line in lines]
    
    return lines

def get_best_digit(batteries: list[int], must_leave=0):
    candidates = range(9, 0, -1)
    for candidate in candidates:
        try:
            first_index = batteries.index(candidate)
            if first_index >= len(batteries) - must_leave:
                continue
        except ValueError:
            continue
        
        return candidate, first_index
    raise ValueError("couldn't find something")

def get_best(batteries: list[int]) -> int:
    best_first_digit, index = get_best_digit(batteries, must_leave=1)
    best_second_digit, second_index = get_best_digit(batteries[index+1:], must_leave=0)
    return best_first_digit * 10 + best_second_digit

def get_best_part2(batteries: list[int]) -> int:
    digits = []
    current_index = 0
    for i in range(12):
        digit, index = get_best_digit(batteries[current_index:], must_leave=12-1-i)
        digits.append(str(digit))
        current_index += index + 1
    return int("".join(digits))

def part1():
    inputs = get_inputs()
    total = 0
    for batteries in inputs:
        best =  get_best(batteries)
        print(best)
        total += best
    print(total)

def part2():
    inputs = get_inputs()
    total = 0
    for batteries in inputs:
        best =  get_best_part2(batteries)
        print(best)
        total += best
    print(total)

if __name__ == "__main__":
    # part1()
    part2()