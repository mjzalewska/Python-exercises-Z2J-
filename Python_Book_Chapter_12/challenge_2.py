"""
Challenge 12.7
"""
import csv
from pathlib import Path

downloads = Path.home() / 'Downloads'
csv_path = list(downloads.rglob('scores.*'))[0]

high_scores_path = Path.home() / 'high_scores.csv'
high_scores_path.touch()


def convert_to_num(line):
    line['score'] = int(line['score'])
    return line


high_scores = []
scores_by_name = {}
max_scores = []

with csv_path.open(mode='r', encoding='utf-8', newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        num_scores = convert_to_num(row)
        high_scores.append(num_scores)

    for item in high_scores:
        scores_by_name[item['name']] = []

    for item in high_scores:
        if item['name'] in scores_by_name.keys():
            scores_by_name[item['name']].append(item['score'])

    for k, v in scores_by_name.items():
        max_scores.append({'name': k, 'score': max(v)})

with high_scores_path.open(mode='w', encoding='utf-8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['name', 'score'])
    writer.writeheader()
    writer.writerows(max_scores)

with high_scores_path.open(mode='r', encoding='utf-8', newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)