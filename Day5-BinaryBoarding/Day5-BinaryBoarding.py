import os, sys, inspect
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))))
from typing import List
from input_reader import read_input



def decode(code: str, lower_bound_code: str, upper_bound_code) -> int:
    code_length: int = len(code)
    lower_bound: int = 0
    upper_bound: int = pow(2, code_length)

    for index in range(code_length):
        if code[index] == upper_bound_code:
            lower_bound = (upper_bound - lower_bound) / 2 + lower_bound
        elif code[index] == lower_bound_code:
            upper_bound = (upper_bound - lower_bound) / 2 + lower_bound

    return lower_bound


def decode_seat(seat_code: str) -> int:
    row_count: int = 7
    column_count: int = 3
    row = decode(seat_code[:row_count], 'F', 'B')
    column = decode(seat_code[row_count:row_count + column_count], 'L', 'R')
    seat = row * 8 + column
    return int(seat)


values: list = [(line, decode_seat(line)) for line in read_input("input.txt")]
values.sort(key=lambda v: v[1], reverse=True)

for index in range(len(values)):
    if(index > 0 and values[index][1] != values[index - 1][1] - 1):
        print(f">>> YOUR SEAT {values[index - 1][1] - 1}")
    print(f"{values[index][0]} -> {values[index][1]}")
