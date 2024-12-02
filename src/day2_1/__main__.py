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


def safe_increase(report: list[int]) -> bool:
    is_safe_inc = True
    for i in range(1, len(report)):
        dif = abs(report[i - 1] - report[i])
        if 1 <= dif <= 3 and report[i] > report[i - 1]:
            continue
        is_safe_inc = False
        break
    return is_safe_inc


def safe_decrease(report: list[int]) -> bool:
    is_safe_dec = True
    for i in range(1, len(report)):
        dif = abs(report[i - 1] - report[i])
        if 1 <= dif <= 3 and report[i] < report[i - 1]:
            continue
        is_safe_dec = False
        break
    return is_safe_dec


def main(f: BinaryIO):
    reports = parse(f)
    t1 = time.perf_counter()
    safe_reports = 0
    for report in reports:
        is_safe_inc = safe_increase(report)
        if is_safe_inc:
            safe_reports += 1
            continue
        is_safe_dec = safe_decrease(report)
        if is_safe_dec:
            safe_reports += 1
            continue
    t2 = (time.perf_counter() - t1)
    print(safe_reports, t2)


if __name__ == '__main__':
    # filename = "test-data.txt"
    filename = "input.txt"
    with open(filename, 'rb') as f:
        main(f)
