from typing import List

def read_input(input_file_path: str) -> List[int]:
    with open(input_file_path, "r") as input_file:
        file_content:str = input_file.read()
        values:List[int] = [int(value) for value in file_content.splitlines()]
        return values

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

input_values: List[int] = read_input("input.txt")
value_pair: (int, int) = find_two_values_whose_sum_equals(input_values, 2020)
value_trio: (int, int, int) = find_three_values_whose_sum_equals(input_values, 2020)
print(f"{value_pair[0]} + {value_pair[1]} = {value_pair[0] + value_pair[1]} // {value_pair[0]} x {value_pair[1]} = {value_pair[0] * value_pair[1]}")
print(f"{value_trio[0]} + {value_trio[1]} + {value_trio[2]} = {value_trio[0] + value_trio[1] + value_trio[2]} // {value_trio[0]} x {value_trio[1]} x {value_trio[2]} = {value_trio[0] * value_trio[1] * value_trio[2]}")
