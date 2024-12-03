import re

from utils import get_input, end_day

corrupted_memory = ''.join(get_input())


def part_0():
    # Regex that I definitely built myself 👀
    return sum([int(a) * int(b) for a, b in re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', corrupted_memory)])


def part_1():
    total_sum, state = 0, True

    for match in re.finditer(r"mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\)", corrupted_memory):
        if state and match.group(0).startswith('mul'):
            total_sum += int(match.group(1)) * int(match.group(2))
        else:
            state = match.group(0) == 'do()'

    return total_sum


end_day(part_0, part_1)
