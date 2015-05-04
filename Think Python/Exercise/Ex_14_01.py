# modify walk()

import os

def walk(directory):
    file_name = []
    for name in os.listdir(directory):
        path = os.path.join(directory, name)
        
        if os.path.isfile(path):
            file_name.append(name)
        else:
            file_name.extend(walk(path))
    return file_name


# Test code
if __name__ == '__main__':
    cwd = os.getcwd()
    files = walk(cwd)
    for f in files:
        print(f)

