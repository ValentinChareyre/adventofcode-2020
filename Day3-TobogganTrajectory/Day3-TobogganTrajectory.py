import os, sys, inspect
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))))) 
from typing import List
from input_reader import read_input

tree_character:str = '#'

def count_trees_on_slope(horizontal_increment: int, vertical_increment:int) -> int:
    line_index:int = 0
    column_index:int = 0
    trees_count:int = 0

    while line_index < len(lines):
        line:str = lines[line_index]
        if line[column_index % len(line)] == tree_character:
            trees_count += 1
        line_index += vertical_increment
        column_index += horizontal_increment
    return trees_count


lines:List[str] = read_input("input.txt")

trees_count_slope_1_1:int = count_trees_on_slope(1, 1)
trees_count_slope_3_1:int = count_trees_on_slope(3, 1)
trees_count_slope_5_1:int = count_trees_on_slope(5, 1)
trees_count_slope_7_1:int = count_trees_on_slope(7, 1)
trees_count_slope_1_2:int = count_trees_on_slope(1, 2)

print("Trees on slope 1, 1 = " + str(trees_count_slope_1_1))
print("Trees on slope 3, 1 = " + str(trees_count_slope_3_1))
print("Trees on slope 5, 1 = " + str(trees_count_slope_5_1))
print("Trees on slope 7, 1 = " + str(trees_count_slope_7_1))
print("Trees on slope 1, 2 = " + str(trees_count_slope_1_2))

print(f"{trees_count_slope_1_1} x {trees_count_slope_3_1} x {trees_count_slope_5_1} x {trees_count_slope_7_1} x {trees_count_slope_1_2} = {trees_count_slope_1_1 * trees_count_slope_3_1 * trees_count_slope_5_1 * trees_count_slope_7_1 * trees_count_slope_1_2}")