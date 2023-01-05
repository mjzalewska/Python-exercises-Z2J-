"""
Challenge 12.7
"""
import csv
from pathlib import Path

downloads = Path.home() / 'Downloads'
csv_path = list(downloads.rglob('scores.*'))[0]


def convert_to_num(row):
    num_value = row['score'] = int(row['score'])
    return num_value


with csv_path.open(mode='r', encoding='utf-8', newline='') as f:
    high_scores = []
    reader = csv.DictReader(f)
    for row in reader:
        print(row)



