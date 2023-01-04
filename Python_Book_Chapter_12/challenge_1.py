"""
Challenge 12.4
Create a new folder in the practice_files folder called images/, and move all image files to that folder.
When done the new folder should have four files:
image1.png
image2.gif
image3.png
image4.jpg
"""
import pathlib

home_path = pathlib.Path.home()
practice_files = home_path / 'Downloads' / 'practice_files'
images = practice_files / 'images'
images.mkdir(exist_ok=True)

paths = list(practice_files.rglob('image*.*'))
for path in paths:
    source = path
    destination = images / path.name
    source.replace(destination)

