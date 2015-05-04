# use os.walk() to print the names of the files in a given directory nand its subdirs

import os

def walk_print(directory):
    file_name = []
    for root, dir, file_list in os.walk(directory):
        file_name.extend(file_list)
    for f in file_name:
        print(f)
        

# Test file
if __name__ == '__main__':
    cwd = os.getcwd()
    walk_print(cwd)
    
