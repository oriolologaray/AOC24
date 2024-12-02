from utils import get_input, end_day

reports = [report.split(' ') for report in get_input()]


def is_safe(report):
    if 0 in (report_diffs := [int(report[i + 1]) - int(report[i]) for i in range(len(report)) if i < len(report) - 1]):
        return False

    if (max_diff := max(report_diffs)) * (min_diff := min(report_diffs)) < 0 or max_diff > 3 or min_diff < -3:
        return False

    return True


def problem_dampener(report):
    # Inefficient but one-liner :(
    return any([is_safe([item for i, item in enumerate(report) if i != removed_i]) for removed_i in range(len(report))])


def part_0():
    return [is_safe(report) for report in reports].count(True)


def part_1():
    return [is_safe(report) or problem_dampener(report) for report in reports].count(True)


end_day(part_0, part_1)
