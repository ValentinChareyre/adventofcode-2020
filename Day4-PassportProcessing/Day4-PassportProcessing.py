import os, sys, inspect
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))))
from typing import List
from input_reader import read_input
import re


lines: List[str] = read_input("input.txt")
documents: List[dict] = []
document: dict = {}
field_regex: re.Pattern = re.compile("([a-z]+):([a-z\\d#]+)")
required_fields: set = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
eye_colors: List[str] = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
valid_document_count: int = 0


def birth_year_is_valid(document: dict) -> bool:
    birth_year = int(document["byr"])
    return birth_year >= 1920 and birth_year <= 2002


def issue_year_is_valid(document: dict) -> bool:
    issue_year = int(document["iyr"])
    return issue_year >= 2010 and issue_year <= 2020


def expiration_year_is_valid(document: dict) -> bool:
    expiration_year = int(document["eyr"])
    return expiration_year >= 2020 and expiration_year <= 2030


def height_is_valid(document: dict) -> bool:
    height = int(document["hgt"][:-2])
    units = document["hgt"][-2:]
    if units == "cm":
        return height >= 150 and height <= 193
    elif units == "in":
        return height >= 59 and height <= 76
    return False


def hair_color_is_valid(document: dict) -> bool:
    return re.match("^#[a-f0-9]{6}$", document["hcl"])


def eye_color_is_valid(document: dict) -> bool:
    return document["ecl"] in eye_colors


def passport_id_is_valid(document: dict) -> bool:
    return re.match("^[0-9]{9}$", document["pid"])


def is_document_valid(document: dict) -> bool:
    if (document.keys() & required_fields) != required_fields:
        return False

    return (birth_year_is_valid(document)
            and issue_year_is_valid(document)
            and expiration_year_is_valid(document)
            and height_is_valid(document)
            and hair_color_is_valid(document)
            and eye_color_is_valid(document)
            and passport_id_is_valid(document))


def process_document(document: dict):
    if is_document_valid(document):
        global valid_document_count
        valid_document_count += 1
        print("\033[92mOK\033[0m " + str(document))
    else:
        print("\033[91mKO\033[0m " + str(document))
    documents.append(document)


def add_fields_to_document(line: str):
    matches = field_regex.findall(line)
    for group in matches:
        document[group[0]] = group[1]


valid_document_count = 0
for line in lines:
    if(len(line) == 0):
        process_document(document)
        document = {}
    else:
        add_fields_to_document(line)
process_document(document)

print(str(valid_document_count) + " valid documents")
