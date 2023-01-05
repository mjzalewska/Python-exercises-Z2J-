"""
Notes - reding/ writing text files
"""
# opening a file object using pathlib
from pathlib import Path

file_path = Path.home() / 'hello.txt'
file_path.touch()

file = file_path.open(mode='r', encoding='utf-8')
# print(type(file)) # <class '_io.TextIOWrapper'>
file.close()

# opening a file object using open()
file_path_1 = r'C:\Users\mjarzebska004\hello.txt'
file_1 = open(file_path_1, mode='r', encoding='utf-8')
file_1.close()

# opening a file using the with statement (context manager)
with file_path.open(mode='w', encoding='utf-8') as file:
    file.write("Hello world\nWhat\'s up?")

# with open(file_path_1, mode='r', encoding='utf-8') as file_1:
#     text = file_1.read()
#     print(text)

# with open(file_path_1, mode='r', encoding='utf-8') as file_1:
#     for line in file_1.readlines():
#         print(line, end='')

list_of_strings = ['\nWell, hi there\n', 'Oh!Hi\n', 'Nice to see you again!\n']

with file_path.open(mode='a', encoding='utf-8') as f:
    f.writelines(list_of_strings)

# with file_path.open(mode='r', encoding='utf-8') as f:
#     for line in f.readlines():
#         print(line, end='')

"""
Review exercises - reading/writing text files
"""
# 1
path = Path.home() / 'starships.txt'

file_input = ['Discovery\n', 'Enterprise\n', 'Defiant\n', 'Voyager\n']

with path.open(mode='w', encoding='utf-8') as f:
    f.writelines(file_input)
# 2
# with path.open(mode='r', encoding='utf-8') as f:
#     for line in f.readlines():
#         print(line, end='')

# 3
# with path.open(mode='r', encoding='utf-8') as f:
#     for line in f.readlines():
#         if line[0] == 'D':
#             print(line, end='')


"""
Notes - reading/ writing CSV files
"""
temperature_readings = [68, 65, 68, 70, 74, 72]

temp_file = Path.home() / 'temperatures.csv'

# with temp_file.open(mode='a', encoding='utf-8') as f:
#     f.write(str(temperature_readings[0]))
#     for temp in temperature_readings[1:]:
#         f.write(f',{temp}')

# with temp_file.open(mode='r', encoding='utf-8') as f:
#     contents = f.read()
#     print(contents)

# reading/ writing files using the CSV module
import csv

daily_temperatures = [[68, 65, 68, 70, 74, 72],
                      [67, 67, 70, 72, 72, 70],
                      [68, 70, 74, 76, 74, 73]]
#
# file = temp_file.open(mode='w', encoding='utf-8', newline='')
# writer = csv.writer(file)
#
# for temp_list in daily_temperatures:
#     writer.writerow(temp_list)
#
# file.close()

# using the with statement:

# with temp_file.open(mode='w', encoding='utf-8', newline='') as f:
#     writer = csv.writer(f)
#     for temp_list in daily_temperatures:
#         writer.writerow(temp_list)

with temp_file.open(mode='w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(daily_temperatures)

daily_temps = []
with temp_file.open(mode='r', encoding='utf-8', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        int_row = [int(temp) for temp in row]
        daily_temps.append(int_row)

# print(daily_temps)

# Reading/ writing csv files with headers


emp_file = Path.home() / 'employees.csv'


# file = emp_file.open(mode='r', encoding='utf-8', newline='')
# reader = csv.DictReader(file)

# when DictReader is used the first row of the CSV file is assumed to contain field names:
# print(reader.fieldnames)
#
# for row in reader:
#     print(row)
# file.close()


def process_row(row):
    row['salary'] = float(row['salary'])
    return row


# with emp_file.open(mode='r', encoding='utf-8', newline='') as f:
#     reader = csv.DictReader(f)
#     for row in reader:
#         print(process_row(row))

people = [
    {'name': 'Veronica', 'age': 29},
    {'name': 'Audrey', 'age': 32},
    {'name': 'Sam', 'age': 24}
]

ppl_file = Path.home() / 'people.csv'

# file_2 = ppl_file.open(mode='w', encoding='utf-8', newline='')
# writer = csv.DictWriter(file_2, fieldnames=people[0].keys())
# writer.writeheader()
# writer.writerows(people)
# file.close()

# with ppl_file.open(mode='r', encoding='utf-8', newline='') as f:
#     reader = csv.DictReader(f)
#     for row in reader:
#         print(row)

"""Review exercises
Reading/ writing CSV files"""

# 1
numbers = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15]
]

num_path = Path.home() / 'numbers.csv'

with num_path.open(mode='w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(numbers)

# 2
int_numbers = []
with num_path.open(mode='r', encoding='utf-8', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        ints = [int(num) for num in row]
        int_numbers.append(ints)

# print(int_numbers)

# 3
colors_path = Path.home() / 'colors.csv'
colors_path.touch(exist_ok=True)

favorite_colors = [
    {'name': 'Joe', 'favorite color': 'blue'},
    {'name': 'Anne', 'favorite color': 'green'},
    {'name': 'Bailey', 'favorite color': 'red'}
]

with colors_path.open(mode='w', encoding='utf-8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=favorite_colors[0].keys())
    writer.writeheader()
    writer.writerows(favorite_colors)

# 4
empty_list = []
with colors_path.open(mode='r', encoding='utf-8', newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        empty_list.append(row)
print(empty_list)


