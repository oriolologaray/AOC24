from utils import get_input, end_day

left, right = zip(*[[int(val) for val in line.split('   ')] for line in get_input()])


def part_0():
    return sum([abs(left_val - right_val) for left_val, right_val in zip(sorted(left), sorted(right))])


def part_1():
    return sum([left_val * right.count(left_val) for left_val in left])


end_day(part_0, part_1)
