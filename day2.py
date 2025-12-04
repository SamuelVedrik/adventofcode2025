import numpy as np

def get_inputs():
    with open("inputs/day2/real.txt") as f:
        line = f.read()
    inputs = line.strip().split(",")
    result = []
    for item in inputs:
        left, right = item.split("-")
        result.append((left, right))
    return result


def generate_and_check_candidates(left: str, right: str):
    invalid_total = 0
    if len(left) == 1:
        left_digits = 1
    else:
        left_digits = int(left[:(len(left))//2])
    right_digits = int(right[:(len(right)+1)//2]) # grab more digits just in case
    for i in range(min(left_digits, right_digits), max(left_digits, right_digits)+1):
        candidate = str(i)+str(i)
        if int(left) <= int(candidate) <= int(right):
            # print(f"{candidate=}, {left=} {right=}")
            invalid_total += int(candidate)
    return invalid_total

# 757-1242

def generate_candidates_part2(left: str, right: str):
    candidates = set()
    left = int(left)
    right = int(right)
    for to_check in range(left, right+1):
        # cursed numpy check because I'm lazy
        # this is actually so stupid
        to_check_str = str(to_check)
        to_check_arr = np.array([c for c in to_check_str])
        # get instances of the first digit
        # if the digits are repeating, then they must have these sizes
        # ignore the first digit
        split_lengths = np.where(to_check_arr == to_check_arr[0])[0][1:]
        for potential_size in split_lengths:
            if len(to_check_str) % potential_size != 0:
                continue
            reshaped = to_check_arr.reshape(-1, potential_size)
            is_valid = (reshaped == reshaped[0]).all()
            # I don't want to check lmao
            if is_valid:
                candidates.add(to_check)
    return sum(list(candidates))

def part1():
    inputs = get_inputs()
    invalid_total = 0
    for ranges in inputs:
        left, right = ranges
        invalid_total += generate_and_check_candidates(left, right)
    print(invalid_total)

def part2():
    inputs = get_inputs()
    invalid_total = 0
    for ranges in inputs:
        left, right = ranges
        invalid_total += generate_candidates_part2(left, right)
    print(invalid_total)
        
if __name__ == "__main__":
    # part1()
    part2()