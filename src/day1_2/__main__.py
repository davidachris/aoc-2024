import time
from typing import BinaryIO, Tuple

def parse(handle: BinaryIO) -> Tuple[list[int], list[int]]:
    left, right = [], []
    for line in handle:
        line = line.strip(b'\r\n')
        line = line.split(b" ")
        left.append(int(line[0]))
        right.append(int(line[-1]))
    return left, right

def sum_values(left: list[int], right: list[int]) -> Tuple[dict[int, int], dict[int, int]]:
    left_dict = {}
    right_dict = {}
    for val in left:
        left_dict[val] = left_dict.get(val, 0) + 1
    for val in right:
        right_dict[val] = right_dict.get(val, 0) + 1
    return left_dict, right_dict

def main(handle: BinaryIO):
    left, right = parse(handle)
    t1 = time.perf_counter()
    left.sort(); right.sort()
    left, right = sum_values(left, right)
    count = 0
    for key, val in left.items():
        rval = right.get(key, 0)
        vsum = key * rval
        count += vsum * val
    t2 = (time.perf_counter() - t1)
    print(t2)
    print(count)


if __name__ == '__main__':
    # filename = 'day1-ex.txt'
    filename = 'day1.txt'
    with open(filename, mode='rb') as f:
        main(f)
