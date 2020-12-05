import os, sys, inspect
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))))) 
from input_reader import read_input
import re

def password_match(line: str, password_policy_and_password_regex: re.Pattern) -> bool:
    match = password_policy_and_password_regex.match(line)
    
    if match == None:
        return False

    min_letter_count = int(match.group(1))
    max_letter_count = int(match.group(2))
    letter           = match.group(3)
    password         = match.group(4)
    occurences_count = password.count(letter)
    result           = min_letter_count <= occurences_count <= max_letter_count

    print("{password:<30} {occurences_count:>3}{letter} {belongs} [{min_letter_count}, {max_letter_count}] {result}".format(
        password = password,
        occurences_count = occurences_count,
        letter = letter,
        belongs = ("∈" if result else "∉"),
        min_letter_count = min_letter_count,
        max_letter_count = max_letter_count,
        result = ('\033[92mOK\033[0m' if result else '\033[91mKO\033[0m')))
    return result


password_policy_and_password_regex:re.Pattern = re.compile("(\d+)\-(\d+) (\w): (\w+)")
correct_password_count = 0
for line in read_input("input.txt"):
    if password_match(line, password_policy_and_password_regex):
        correct_password_count += 1

print(f"{correct_password_count} passwords are correct")