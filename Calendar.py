import os
import glob
from os import system, name 
from typing import List

def clear(): 
    if name == 'nt': # windows 
        _ = system('cls')
    else: # for mac and linux(here, os.name is 'posix') 
        _ = system('clear') 

def get_calendar_directory() -> str:
    calendar_file:str = os.path.realpath(__file__)
    return os.path.dirname(calendar_file)

def get_calendar_programs() -> List[str]:
    calendar_directory:str = get_calendar_directory()
    python_scripts: List[str] = []
    for dirpath, dirnames, filenames in os.walk(calendar_directory):
        for filename in filenames:
            if filename.startswith("Day") and filename.endswith(".py") and "-part" not in filename:
                python_scripts.append(dirpath + "\\" + filename)
    return python_scripts

def print_programs(programs: List[str]):
    for program_index in range(len(programs)):
        print(f"  {program_index + 1}: {os.path.basename(programs[program_index])[:-3]}")

# ==================================================================== #

clear()
print("===== Advent of Code 2020 =====\n")
programs: List[str] = get_calendar_programs()
print_programs(programs)
programs_count = len(programs)

if programs_count > 0:
    index = int(input("\nWhich script do you want to execute? (0 to exit): "))
    if index > programs_count:
        print("No script for that day!")
    elif index > 0:
        os.chdir(os.path.dirname(programs[index - 1]))
        with open(programs[index - 1], "r") as script:
            exec(script.read())