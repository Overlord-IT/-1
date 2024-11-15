import csv
import json


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME, 'r') as csvfile:
        reader = csv.DictReader (csvfile)
        data = list(reader)

    with open(OUTPUT_FILENAME, 'w') as outfile:
        json.dump(data, outfile, indent=4)

if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
