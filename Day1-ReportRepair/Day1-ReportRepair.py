from typing import List
import os, sys, inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) 
from input_reader import read_input

def find_two_values_whose_sum_equals(input_values: List[int], result: int) -> (int, int):
    values_count = len(input_values)
    for first_operand_index in range(values_count):
        for second_operand_index in range(first_operand_index, values_count):
            if input_values[first_operand_index] + input_values[second_operand_index] == result:
                return input_values[first_operand_index], input_values[second_operand_index]

def find_three_values_whose_sum_equals(input_values: List[int], result: int) -> (int, int, int):
    values_count = len(input_values)
    for first_operand_index in range(values_count):
        for second_operand_index in range(first_operand_index, values_count):
            for third_operand_index in range(second_operand_index, values_count):
                if input_values[first_operand_index] + input_values[second_operand_index] + input_values[third_operand_index] == result:
                    return input_values[first_operand_index], input_values[second_operand_index], input_values[third_operand_index]

# ==========================================================================================

input_values: List[int] = [int(value) for value in read_input("input.txt")]
value_pair: (int, int) = find_two_values_whose_sum_equals(input_values, 2020)
value_trio: (int, int, int) = find_three_values_whose_sum_equals(input_values, 2020)
print(f"{value_pair[0]} + {value_pair[1]} = {value_pair[0] + value_pair[1]} // {value_pair[0]} x {value_pair[1]} = {value_pair[0] * value_pair[1]}")
print(f"{value_trio[0]} + {value_trio[1]} + {value_trio[2]} = {value_trio[0] + value_trio[1] + value_trio[2]} // {value_trio[0]} x {value_trio[1]} x {value_trio[2]} = {value_trio[0] * value_trio[1] * value_trio[2]}")
