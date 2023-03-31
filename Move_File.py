import os
import shutil

from_dir = 'C:/Users/dell/Downloads'
to_dir = 'C:/Users/dell/OneDrive/Documents'

list_of_files = os.listdir(from_dir)
#print(list_of_files)

for file in list_of_files:
    name, extension = os.path.splitext(file)
    print(name)
    print(extension)