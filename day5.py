

def get_inputs():
    with open("inputs/day5/real.txt") as f:
        data = f.read()
        ranges, items = data.split("\n\n")
        ranges = ranges.split("\n")
        items = items.split("\n")
        items = [int(item) for item in items]
    parsed_ranges = []
    for range_ in ranges:
        left, right = range_.split("-")
        parsed_ranges.append((int(left), int(right)))
    return parsed_ranges, items

def part1():
    ranges, items = get_inputs()
    num_fresh = 0
    for item in items:
        for left, right in ranges:
            if left <= item <= right:
                num_fresh += 1
                break
    print(num_fresh)

def overlaps(range_a: tuple, range_b: tuple):
    return not ((range_a[1] < range_b[0]) or (range_b[1] < range_a[0]))

def merge(range_a, range_b):
    return min(range_a[0], range_b[0]), max(range_a[1], range_b[1])

def part2():
    ranges, _ = get_inputs()
    complete_ranges = set()
    complete_ranges.add(ranges[0])
    
    unseen = set(ranges[1:])

    while len(unseen) > 0:
        range_ = unseen.pop()
        overlap_found = False
        for range_to_check in complete_ranges:
            if overlaps(range_to_check, range_):
                merged_range = merge(range_to_check, range_)
                complete_ranges.remove(range_to_check)
                overlap_found = True
                unseen.update(complete_ranges)
                complete_ranges = set()
                complete_ranges.add(merged_range)
                break
        if not overlap_found:
            complete_ranges.add(range_)
    
    total = 0
    for range_ in complete_ranges:
        print(range_)
        total += (range_[1] - range_[0]) + 1
    print(total)


if __name__ == "__main__":
    # part1()
    part2()