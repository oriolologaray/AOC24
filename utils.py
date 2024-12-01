from typing import Callable


def get_input() -> list[str]:
    with open("input.txt", 'r', encoding='utf-8') as file:
        lines = file.read().splitlines()
    return lines


def end_day(part_0: Callable, part_1: Callable) -> None:
    sassy_reply = "This should be returning a solution... Unless you can't solve today's challenge?"
    print("=========================================================")
    print(f"Part 0: {result if (result := part_0()) else sassy_reply}")
    print(f"Part 1: {result if (result := part_1()) else sassy_reply}")
    print("=========================================================")
