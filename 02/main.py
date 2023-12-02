import re

INPUT_FILE = "input.txt"

MAX_R = 12
MAX_G = 13
MAX_B = 14


def main():
    out = 0
    power = 0

    with open(INPUT_FILE) as f:
        for i, ll in enumerate(f, 1):

            blues = [int(x) for x in re.findall(r'\d+(?=\sblue)', ll)]
            greens = [int(x) for x in re.findall(r'\d+(?=\sgreen)', ll)]
            reds = [int(x) for x in re.findall(r'\d+(?=\sred)', ll)]

            power += max(blues) * max(greens) * max(reds)

            ok = True
            ok = ok and all(x <= MAX_B for x in blues)
            ok = ok and all(x <= MAX_G for x in greens)
            ok = ok and all(x <= MAX_R for x in reds)

            if ok:
                out += i

    print(f"Part 1: {out}")
    print(f"Part 2: {power}")


if __name__ == "__main__":
    main()
