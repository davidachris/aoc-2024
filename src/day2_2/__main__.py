import time
from typing import BinaryIO


def parse(handle: BinaryIO) -> list[list[int]]:
    reports = []
    for line in handle:
        line = line.strip(b'\r\n')
        line = line.split(b" ")
        report = [int(val) for val in line]
        reports.append(report)
    return reports


def is_distance(a: int, b: int) -> bool:
    return 1 <= abs(a - b) <= 3


def safe_distance(report: list[int]) -> bool:
    is_safe = False
    for i in range(1, len(report)):
        is_safe = is_distance(report[i], report[i - 1])
        if not is_safe:
            break
    return is_safe


def safe_direction(report: list[int]) -> bool:
    has_items = len(report) > 1
    is_safe = False
    if not has_items or report[0] == report[1]:
        return is_safe
    asc = report[0] < report[1]
    is_safe = True
    for i in range(1, len(report)):
        if asc and report[i] > report[i - 1]:
            continue
        if not asc and report[i] < report[i - 1]:
            continue
        is_safe = False
        break
    return is_safe


def safety_report(report: list[int], check: bool = False) -> bool:
    is_safe = False
    is_safe_direction = safe_direction(report)
    is_safe_distance = safe_distance(report)
    if is_safe_distance and is_safe_direction:
        is_safe = True
        return is_safe
    if check:
        return is_safe
    for i in range(len(report)):
        new_report = report[:i] + report[i + 1:]
        is_safe = safety_report(new_report, True)
        if is_safe:
            break
    return is_safe


def main(f: BinaryIO):
    reports = parse(f)
    t1 = time.perf_counter()
    safe_reports = 0
    for report in reports:
        is_safe = safety_report(report)
        if not is_safe:
            continue
        safe_reports += 1
    t2 = (time.perf_counter() - t1)
    print(safe_reports, t2)


if __name__ == '__main__':
    # filename = "test-data.txt"
    filename = "input.txt"
    with open(filename, 'rb') as f:
        main(f)
