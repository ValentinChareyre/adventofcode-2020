import os, sys, inspect
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))))) 
from input_reader import read_input
import re

def highlight(input: str, character_index: int, match: bool) -> str:
    return input[:character_index] + ("\033[92m" if match else "\033[91m") + input[character_index] + "\033[0m" + input[character_index + 1:]

def password_match(line: str, password_policy_and_password_regex: re.Pattern) -> bool:
    match = password_policy_and_password_regex.match(line)
    
    if match == None:
        return False

    first_index      = int(match.group(1))
    second_index     = int(match.group(2))
    letter           = match.group(3)
    password         = match.group(4)
    first_letter_match = password[first_index - 1] == letter
    second_letter_match = password[second_index - 1] == letter
    result           = first_letter_match ^ second_letter_match

    print("{password:<40} {letter} {result}".format(
        password = highlight(highlight(password, second_index - 1, second_letter_match), first_index - 1, first_letter_match),
        letter = letter,
        result = ('\033[92mOK\033[0m' if result else '\033[91mKO\033[0m')))
    return result

password_policy_and_password_regex:re.Pattern = re.compile("(\d+)\-(\d+) (\w): (\w+)")
correct_password_count = 0
for line in read_input("input.txt"):
    if password_match(line, password_policy_and_password_regex):
        correct_password_count += 1

print(f"{correct_password_count} passwords are correct")