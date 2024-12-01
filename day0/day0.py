left = right = []

with open("input.txt") as file:
    while line := file.readline():
        left_input, right_input = line.rstrip().split("   ")
        left, right = [*left, int(left_input)], [*right, int(right_input)]


def part_0():
    return sum(
        [
            abs(left_val - right_val)
            for left_val, right_val in zip(sorted(left), sorted(right))
        ]
    )


def part_1():
    return sum([left_val * right.count(left_val) for left_val in left])


print(part_0(), part_1())
