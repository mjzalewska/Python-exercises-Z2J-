import pathlib

path = pathlib.Path(r'C:\Users\mjarzebska004\Downloads\all-coding-books.txt)')

home = pathlib.Path.home()
print(home)
print(type(home))

currend_wd = pathlib.Path.cwd()
print(currend_wd)
print(type(currend_wd))

# adding subdirectories
print(home/'Downloads'/'all-coding-books.txt')
# checking if path is absolute
print(home.is_absolute())
# extending a relative path
print(home/pathlib.Path('Downloads/test_adv.txt'))
# checking parent directories
print(list(home.parents))
# checking the root directory
print(home.anchor)
# checking name of file or directory
print(home.name)
# checking the stem(name) of a file
print(path.stem)
# checking file extension
print(path.suffix)

# checking if a path exists
print(home.exists())
# checking if path refers to a file or a directory
# returns False if the file doesn't exist
print(path.is_file())
# checking if path refers to a dir
print(home.is_dir())