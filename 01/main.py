INPUT_FILE = "input.txt"


def find_first(line, digits, reverse=False):
    if reverse:
        line = line[::-1]
        digits = [d[::-1] for d in digits]

    idx = len(line)
    occ = 0
    for i, d in enumerate(digits):
        first_occ = idx

        if d in line:
            first_occ = min(line.find(d), first_occ)
        if str(i + 1) in line:
            first_occ = min(line.find(str(i + 1)), first_occ)

        if first_occ < idx:
            idx, occ = first_occ, i + 1

    assert occ > 0, f"occ is {occ}: {line}"
    print(occ)
    return occ


def main():
    # part 1
    total = 0
    with open(INPUT_FILE) as f:
        for ll in f:
            digits = [c for c in ll if c.isdigit()]
            total += int(digits[0] + digits[-1])

    print(f"Part 1: {total}")

    # part 2
    digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    total = 0
    with open(INPUT_FILE) as f:
        for ll in f:
            ll = ll.strip()
            total += find_first(ll, digits) * 10 + find_first(ll, digits, True)

    print(f"Part 2: {total}")


if __name__ == "__main__":
    main()
