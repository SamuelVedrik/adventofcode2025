
def get_inputs():
    with open('inputs/day1/real.txt') as f:
        inputs = f.readlines()
    return inputs

def part1():
    inputs = get_inputs()
    current = 50
    num_at_0 = 0
    for item in inputs:
        sign, number = item[0], int(item[1:])
        if sign == "L":
            current = current - number
        if sign == "R":
            current = current + number
        current = current % 100
        if current == 0:
            num_at_0 += 1
    print(num_at_0)

def part2():
    inputs = get_inputs()
    previous = 50
    current = 50
    num_at_0 = 0
    for item in inputs:
        previous = current
        sign, number = item[0], int(item[1:])
        rotations = number // 100 # number of complete revolutions
        num_at_0 += rotations # we just add number of rotations to times we hit 0. Ex: We treat L466 the same as L66
        number = number % 100
        if sign == "L":
            current = current - number
        if sign == "R":
            current = current + number
        if (current >= 100 or current <= 0) and (previous != 0):
            num_at_0 += 1
        current = current % 100
    print(num_at_0)

if __name__ == "__main__":
    # part1()
    part2()