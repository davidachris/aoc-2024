from typing import BinaryIO


def parse(handle: BinaryIO) -> bytes:
    mem = b''
    for line in handle:
        line = line.strip(b'\r\n')
        mem += line
    return mem


def mul(a, b):
    return int(a) * int(b)


def parse_mul(idx: int, mem: str):
    comma = False
    end_paren = False
    arg1 = ""
    arg2 = ""
    for i in range(idx, len(mem)):
        char = mem[i]
        if char.isdigit() and not comma:
            arg1 += char
            continue
        if char.isdigit() and comma:
            arg2 += char
            continue
        if char == ',':
            comma = True
            continue
        if char == ')':
            end_paren = True
            break
        break
    if not comma or not end_paren:
        return None
    return arg1, arg2


def main(f: BinaryIO):
    mem = parse(f)
    mem = mem.decode('utf-8')
    count = 0
    do = True
    for i in range(len(mem) - 3):
        do_t = mem[i:i + 4]
        dont_t = mem[i:i + 7]
        mul_t = mem[i:i + 4]
        if do and dont_t == "don't()":
            i += 8
            do = False
        if not do and do_t == "do()":
            i += 5
            do = True
        if do and mul_t == "mul(":
            i += 4
            args = parse_mul(i, mem)
            if not args:
                continue
            count += mul(*args)
    print(count)


if __name__ == '__main__':
    # filename = "test.txt"
    filename = "input.txt"
    with open(filename, mode='rb') as f:
        main(f)
