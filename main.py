"""
Project description:
    - must have function to generate random objects of different attributes (colored boxes)
        - generate hex codes?
    - need a hasing function (binary)
    - count the runs of 0's from right to left
    - 1/2^n where n = longest run of 0 is approx the amt of unique objects
    - run concurrently in paralell (threads?) then avg the scorecards
    - tests?
"""
from random import choice
from itertools import groupby


def create_hex_codes() -> str:
    alphanumeric = ["A", "B", "C", "D", "E", "F"] + list(map(str, range(0, 10)))
    hex = "0x"
    for _ in range(6):
        hex += choice(alphanumeric)

    return hex


def hash(hex_code: str) -> str:
    # DOC: converts the string hex code into an integer then into a binary string which is then formated and reversed
    return bin(int(hex_code, 16))[2:][::-1]


def count_zeros(binary_str: str) -> int:
    sub_score = 0
    for digit in binary_str:
        if digit == "0":
            sub_score += 1
        else:
            break

    return sub_score


def hyper_log_log(binary_hex_codes: list[str]):
    score = 0
    for hex_code in binary_hex_codes:
        score = count_zeros(hex_code) if count_zeros(hex_code) > score else score

    return score


def main():
    binary_hex_codes = [create_hex_codes() for _ in range(10)]
    binary_hex_codes = [hash(hex_code) for hex_code in binary_hex_codes]

    print(binary_hex_codes)

    score = hyper_log_log(binary_hex_codes)

    print(score)

    return 2**score


if __name__ == "__main__":
    print(main())
