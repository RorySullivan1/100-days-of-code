from pandas import read_csv


def input_to_nato(io_str: str):
    converter = read_csv("nato_conversions.csv")
    return [converter[converter["letter"] == letter]["code"].values[0] for letter in io_str]

response = False
while not response:
    user_io = input("Enter your name...",).upper()
    resp = input(f"{input_to_nato(user_io)} ... Is this correct? (Y/N)")
    response = resp.upper() == "Y"