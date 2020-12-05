index = int(input("\nWhich part do you want to execute? 1 or 2?: "))
if index > 2:
    print(f"No part {index}!")
elif index == 1:
    with open("Day2-PasswordPhilosophy-part1.py", "r", encoding="utf-8") as script:
        exec(script.read())
elif index == 2:
    with open("Day2-PasswordPhilosophy-part2.py", "r") as script:
        exec(script.read())