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

def main(handle: BinaryIO):
    left, right = parse(handle)
    t1 = time.perf_counter()
    left.sort(); right.sort()
    count = 0
    for i in range(len(left)):
        count += abs(left[i] - right[i])
    t2 = (time.perf_counter() - t1)
    print(t2)
    print(count)

if __name__ == '__main__':
    # filename = 'day1-ex.txt'
    filename = 'day1.txt'
    with open(filename, mode='rb') as f:
        main(f)
