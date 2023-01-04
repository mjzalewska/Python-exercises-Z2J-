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

list_of_strings = ['\nWell, hi there\n','Oh!Hi\n', 'Nice to see you again!\n' ]

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
with path.open(mode='r', encoding='utf-8') as f:
    for line in f.readlines():
        if line[0] == 'D':
            print(line, end='')


