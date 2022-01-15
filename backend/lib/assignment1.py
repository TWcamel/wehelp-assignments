from request import get
import write_file as wf
from pathlib import Path
import json


def assignment1():
    url = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
    data = get(url)['result']['results']

    file_name = 'assignment1.csv'
    fle = Path(file_name)
    fle.touch(exist_ok=True)
    wf.extrate_data_to_csv(file_name, data)


if __name__ == "__main__":
    assignment1()
