import pathlib
from pathlib import Path

path = pathlib.Path(r'C:\Users\magda\Downloads\all-coding-books.txt)')

home = pathlib.Path.home()
# print(home)
# print(type(home))

currend_wd = pathlib.Path.cwd()
# print(currend_wd)
# print(type(currend_wd))

# # adding subdirectories
# print(home/'Downloads'/'all-coding-books.txt')
# # checking if path is absolute
# print(home.is_absolute())
# # extending a relative path
# print(home/pathlib.Path('Downloads/test_adv.txt'))
# # checking parent directories
# print(list(home.parents))
# # checking the root directory
# print(home.anchor)
# # checking name of file or directory
# print(home.name)
# # checking the stem(name) of a file
# print(path.stem)
# # checking file extension
# print(path.suffix)
#
# # checking if a path exists
# print(home.exists())
# # checking if path refers to a file or a directory
# # returns False if the file doesn't exist
# print(path.is_file())
# # checking if path refers to a dir
# print(home.is_dir())

"""
Review exercise 1
1.Create a new Path object to a file called my_file.txt in a folder called my_folder/ in your computer's 
home directory. Assign this Path object to the variable name file_path.
2. Check if the path assigned to the file_path exists
3. Print the name of the path assigned to file path . The output should be my_file.txt
4. Print the name of the parent directory of the path assigned to file_path. The output should be my_folder
"""
file_path = pathlib.Path(r'C:\Users\magda\my_folder\my_file.txt')
# print(file_path.exists())
# print(file_path.name)
# print(file_path.parent.name)

# creating a new directory
new_dir = Path.home() / 'new_directory'
# new_dir.mkdir()
# print(new_dir.is_dir())
# print(new_dir.exists())
# new_dir.mkdir(exist_ok=True)  # won't raise FileExistsError if dir already exists

nested_dir = new_dir / 'folder_a' / 'folder_b'  # causes FileExistsError, because folder_a doesn't exist
# nested_dir.mkdir(parents=True, exist_ok=True)  # when parents=True added all non-existent parents are created
# print(new_dir.exists())

file_path_1 = new_dir / 'file_1.txt'
file_path_1.touch()  # to create a file
# print(file_path_1.exists())

file_path_2 = new_dir / 'folder_c' / 'file_2.txt'
# file_path_2.mkdir() # raises an exception as folder_c doesn't exist
# file_path_2.parent.mkdir(exist_ok=True)
# file_path_2.touch()

# iterate over directory contents
# for path in new_dir.iterdir():
#   print(path)

# search for files in a directory
# for path in new_dir.glob('*.txt'):
#     print(path)

# return values of iterdir() and glob() can both be converted to a list

paths = [new_dir / 'program1.py',
         new_dir / 'program2.py',
         new_dir / 'folder_a' / 'program3.py',
         new_dir / 'folder_a' / 'folder_b' / 'image1.jpg',
         new_dir / 'folder_a' / 'folder_b' / 'image2.png']
# for path in paths:
#     path.touch()

# pattern matching
# print(list(new_dir.glob('*.py')))
# print(list(new_dir.glob('*1*')))
#
# print(list(new_dir.glob('program?.py')))
# print(list(new_dir.glob('?older_?')))
# print(list(new_dir.glob('*1.??')))
# print(list(new_dir.glob('program[13].py')))
#
# # recursive matching with **
# print(list(new_dir.glob('**/*.txt')))
# print(list(new_dir.glob('**/*.py')))
# # recursive matching with rglob()
# print(list(new_dir.rglob('*.py')))

# moving & renaming files with .replace()
# move a file
source = new_dir / 'file_1.txt'
destination = new_dir / 'folder_a' / 'file_1.txt'
# if not destination.exists(): # to check if the destination file exists so that it's not overwritten
#     source.replace(destination)
# rename a file
source = new_dir / 'folder_c'
destination = new_dir / 'folder_d'
# if not destination.exists():
#     source.replace(destination)

# delete a file
file_path_3 = new_dir / 'program1.py'
# file_path_3.unlink(missing_ok=True)
print(file_path_3.exists())

# delete a directory with rmdir() - directory must be empty
folder_d = new_dir / 'folder_d'
# for path in folder_d.iterdir():
#     path.unlink(missing_ok=True)
# folder_d.rmdir()
print(folder_d.exists())

# to delete non-empty directory use shutil
import shutil

folder_a = new_dir / 'folder_a'
# shutil.rmtree(folder_a)
print(folder_a.exists())

"""Review exercise 2
1. Create na new directory in your home folder called my_folder
2. Inside my_folder create 3 files: file1.txt, file2.txt, image1.png
3. Move image1.png to a new directory called images inside the my_folder directory
4. Delete the file1.txt 
5. Delete my_folder directory
"""
# 1
home_dir = Path.home()
my_folder = home_dir / 'my_folder'
# my_folder.mkdir(exist_ok=True)

# 2
# new_paths = [my_folder / 'file1.txt', my_folder / 'file2.txt', my_folder / 'image1.png']
# for path in new_paths:
#     path.touch(exist_ok=True)

image2_path = my_folder / 'image2.jpg'
# image2_path.touch()

# 3
# images_folder = my_folder / 'images'
# # images_folder.mkdir(exist_ok=True)
# source_dir = my_folder / 'image2.jpg'
# destin_dir = images_folder
# source_dir.replace(destin_dir)

# 4
# file1 = my_folder / 'file1.txt'
# file1.unlink()

# 5
# shutil.rmtree(my_folder)
