from typing import List

def read_input(input_file_path: str) -> List[int]:
    with open(input_file_path, "r") as input_file:
        file_content:str = input_file.read()
        values:List[int] = file_content.splitlines()
        return values